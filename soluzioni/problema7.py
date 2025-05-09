import os


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "7")
    outputFolder = os.path.join("soluzioni", "output", "7")

    @staticmethod
    def solve(wagons: list[tuple[int, int]]) -> int:
        """
        Scrivi la tua soluzione qui
        """
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
            input = []
            for line in file.readlines():
                temp = line.strip().split(", ")
                input.append(tuple(map(int, temp)))
        return input

    @staticmethod
    def loadOutput(i: int) -> str:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            for line in file:
                return int(line.strip())
