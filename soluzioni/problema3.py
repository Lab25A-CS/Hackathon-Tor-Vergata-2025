import os
import pprint as pp


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "3")
    outputFolder = os.path.join("soluzioni", "output", "3")

    @staticmethod
    def solve(matrix: list[list[int]], k: int, start: str) -> int:
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

        matrix = []
        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            for i, line in enumerate(file):
                if i == 0:
                    len, key = line.strip().split(",")
                else:
                    newLine = []
                    for char in line.strip():
                        newLine.append(char)
                    matrix.append(newLine)
        return matrix, int(len), key

    @staticmethod
    def loadOutput(i: int) -> int:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            value = ""
            for line in file:
                value += line.strip()
        return int(value)
