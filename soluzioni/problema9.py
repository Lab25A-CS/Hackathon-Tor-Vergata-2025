import os


class Solution:

    inputFolder = os.path.join("soluzioni", "input", "9")
    outputFolder = os.path.join("soluzioni", "output", "9")

    @staticmethod
    def solve(costs: list[int], k: int):
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
            maxColor = int(lines[0].strip())
            costs = list(map(int, lines[1].strip().split(", ")))
        return costs, maxColor

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
