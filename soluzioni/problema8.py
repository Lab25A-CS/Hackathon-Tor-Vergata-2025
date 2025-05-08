import os


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "8")
    outputFolder = os.path.join("soluzioni", "output", "8")

    @staticmethod
    def solve(firstStack: list[int], secondStack: list[int], maxWeight: int) -> tuple[int, int]:
        '''
        Scrivi la tua soluzione qui
        '''
        pass

    @staticmethod
    def loadInput(i: int) -> str:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            lines = file.readlines()
            maxWeight = int(lines[0].strip())
            first = list(map(int, lines[1].strip().split(", ")))
            second = list(map(int, lines[2].strip().split(", ")))
        return first, second, maxWeight

    @staticmethod
    def loadOutput(i: int) -> int:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            return int(file.readline().strip())

    @staticmethod
    def evaluateSolution(
        firstStack: list[int],
        secondStack: list[int],
        maxWeight: int,
    ) -> int:

        n = len(firstStack)
        m = len(secondStack)

        firstSum = []
        newFirst = 0
        for t in range(n):
            newFirst += firstStack[t]
            firstSum.append(newFirst)

        secondSum = []
        newSecond = 0
        for k in range(m):
            newSecond += secondStack[k]
            secondSum.append(newSecond)

        i, j = Solution.solve(firstStack, secondStack, maxWeight)
        output = 0
        if i != -1:
            output += firstSum[i]
        if j != -1:
            output += secondSum[j]

        return output
