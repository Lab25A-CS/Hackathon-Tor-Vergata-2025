import time
import soluzioni
import signal
import os
from pprint import pprint
import sys

IS_WINDOWS = sys.platform.startswith("win")

TIMEOUT = [
    2,  # problem 0
    10,  # problem 1
    10,  # problem 2
    100,  # problem 3
    1,  # problem 4
    1,  # problem 5
    100,  # problem 6
    1,  # problem 7
    1,  # problem 8
    9,  # problem 9
    9,  # problem 10
]

difficulties = {
    0: 1,
    1: 2,
    2: 2,
    3: 3,
    4: 3,
    5: 4,
    6: 3,
    7: 4,
    8: 5,
    9: 5,
    10: 10,
}

titles = {
    0: "Franchino ed il primo viaggio indimenticabile",
    1: "Franchino ed il misterioso verdetto del professor Pasquals",
    2: "Franchino ed il parser ubriaco",
    3: "Franchino ed il cruciverba maledetto",
    4: "Franchino alle prese con l'area dei rettangoli",
    5: "Franchino ed il filo di arianna",
    6: "Franchino e l'incubo falsa laurea",
    7: "Franchino e la passione per TrainVergata",
    8: "Franchino ed il backlog videoludico",
    9: "Franchino e la porta del laboratorio",
    10: "Franchino e l'arte della selezione strategica",
}


def colorPrint(text: str, color: str, **kwargs) -> None:
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
    }
    end = kwargs.get("end", "\n")
    print(f"{colors[color]}{text}\033[0m", end=end)
    return


def timeoutHandler(signum, frame):
    raise TimeoutError("Timeout occured!")


def runSolution(problemNumber: int, args) -> any:
    problem = soluzioni.problem[problemNumber]
    if problemNumber not in (10, 8):
        if isinstance(args, (tuple)):
            return problem.solve(*args)
        else:
            return problem.solve(args)
    else:
        return problem.evaluateSolution(*args)


def run(problemNumber: int, args, timeout: int) -> dict[str, any]:
    # mettere if per windows con signal.SIGBREAK (vedi poi, forse)
    sig = signal.SIGBREAK if IS_WINDOWS else signal.SIGALRM  # questa è la modifica
    signal.signal(sig, timeoutHandler)
    signal.alarm(timeout)
    startTime = time.time()
    testInfo = {
        "timeout": False,
        "result": None,
        "time": None,
        "error": False,
        "errorMessage": "",
    }

    try:
        result = runSolution(problemNumber, args)
        delta = time.time() - startTime
        testInfo["result"] = result
        testInfo["time"] = delta
    except TimeoutError:
        testInfo["timeout"] = True
    except Exception as e:
        testInfo["error"] = True
        testInfo["errorMessage"] = str(e)
    finally:
        signal.alarm(0)

    return testInfo


def loadInput(problemNumber: int) -> tuple[any]:

    inputDir = os.path.join("soluzioni", "input", f"{problemNumber}")

    numTest = len(os.listdir(inputDir))

    inputs = []
    for i in range(numTest):
        inputs.append(soluzioni.problem[problemNumber].loadInput(i))
    return inputs


def loadOutput(problemNumber: int) -> tuple[any]:

    outputDir = os.path.join("soluzioni", "output", f"{problemNumber}")

    numTest = len(os.listdir(outputDir))

    outputs = []
    for i in range(numTest):
        outputs.append(soluzioni.problem[problemNumber].loadOutput(i))
    return outputs


def normalizeTime(time: float, factor: int, difficutly: int) -> float:
    return 1 - (time / factor) / (2**difficutly)


def test(problemNumber: int) -> float:
    inputs = loadInput(problemNumber)
    outputs = loadOutput(problemNumber)

    startTime = time.time()

    print("====================================")
    print(f"Running test for problem {problemNumber}")

    print(f"Title:\t\033[1m{titles[problemNumber]}\033[0m")
    maxScore = 100 * difficulties[problemNumber]

    print("Difficulty level:", difficulties[problemNumber])
    print()
    score = 0
    score10 = 0
    normalizationFactor = 0
    timeout = TIMEOUT[problemNumber]
    c = 1.5

    for i, (input, output) in enumerate(zip(inputs, outputs)):
        normalizationFactor += c**i

        print(f"\tRunning test {i}...", end=" ", flush=True)

        testInfo = run(problemNumber, input, timeout=timeout)
        if testInfo["timeout"]:
            colorPrint(f"Timeout occurred for test {i}!", "purple")
        elif testInfo["error"]:
            colorPrint(
                f"An error occurred for test {i}: {testInfo['errorMessage']}", "red"
            )
        else:
            if problemNumber != 10:
                if testInfo["result"] != output:
                    colorPrint(
                        f"Test {i} failed: expected {output}, got {testInfo['result']}",
                        "yellow",
                    )
                else:
                    score += (c**i) * 10 * normalizeTime(testInfo["time"], timeout, i)
                    colorPrint("OK", "green")
            else:
                if testInfo["result"] != float("inf"):
                    score10 = testInfo["result"]
                    colorPrint("OK", "green")
                else:
                    colorPrint(
                        f"Test {i} failed: got {testInfo['result']}",
                        "yellow",
                    )

    finalScore = difficulties[problemNumber] * 10 * score / normalizationFactor

    delta = time.time() - startTime
    print(f"\fProblem {problemNumber} runs in {delta:.2f}sec.")
    if problemNumber != 10:
        colorPrint(
            f"Score for problem {problemNumber}: {finalScore:.2f} / {maxScore}", "cyan"
        )
    else:
        colorPrint(f"Score for problem {problemNumber}: {score10}", "cyan")

    print("====================================")
    print()

    return finalScore


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests for the problems")
    parser.add_argument(
        "-t",
        "--tests",
        nargs="+",
        type=int,
        help="Run only the tests for the specified problems",
    )

    args = parser.parse_args()

    if args.tests:
        scores = 0
        for problemNumber in args.tests:
            scores += test(problemNumber)

        colorPrint(f"Total score: {scores:.2f}", "blue")
    else:
        scores = 0
        for i in range(11):
            scores += test(i)

        colorPrint(f"Total score: {scores:.2f}", "blue")
