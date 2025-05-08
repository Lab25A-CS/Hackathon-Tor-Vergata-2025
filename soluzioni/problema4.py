import os


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "4")
    outputFolder = os.path.join("soluzioni", "output", "4")

    @staticmethod
    def solve(matrix: list[list[int]], squares: list[list[int, int, int, int]]) -> list[int]:
        '''
        Scrivi la tua soluzione qui
        '''
        pass

    @staticmethod
    def loadInput(i: int) -> tuple[list[list[int]], list[list[int, int, int, int]]]:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """
        files = os.listdir(Solution.inputFolder)
        files.sort()

        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            matrix = []
            squares = []
            for i, line in enumerate(file):
                if i == 0:
                    j = int(line.strip())
                elif i <= j:
                    matrix.append(list(map(int, line.strip().split(","))))
                elif i > j:
                    squares.append(list(map(int, line.strip().split(","))))
        return matrix, squares

    @staticmethod
    def loadOutput(i: int) -> list[int]:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """
        files = os.listdir(Solution.outputFolder)
        files.sort()

        with open(os.path.join(Solution.outputFolder, files[i])) as file:
            for line in file:
                list = line.strip().split(",")
                for i in range(len(list)):
                    list[i] = int(list[i])
        return list
