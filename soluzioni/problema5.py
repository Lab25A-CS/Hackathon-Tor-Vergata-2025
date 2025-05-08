import os

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '5')
    outputFolder = os.path.join('soluzioni', 'output', '5')
    
    @staticmethod
    def solve(edges: list[list[str, int, str, str]], targetSum: int) -> int:
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
        edges = []
        targetSum = 0
        with open(os.path.join(Solution.inputFolder, files[i])) as file:
            for i, line in enumerate(file):
                if i == 0:
                    targetSum = int(line.strip())
                else:
                    edges.append(line.strip().split(', '))
        return edges, targetSum

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


