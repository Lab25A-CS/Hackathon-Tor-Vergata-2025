import os
from collections import deque

class Solution:

    inputFolder = os.path.join('soluzioni', 'input', '6')
    outputFolder = os.path.join('soluzioni', 'output', '6')
   
    emotes = {
        "SKULL": "💀",
        "CANDY": "🍬",
        "MUSHROOM": "🍄",
        "MIRROR": "🪞",
        "LEFT": "🠔",
        "UP": "🠕 ",
        "RIGHT": "🠖",
        "DOWN": "🠗 ",
        "END": "🏁"
    }

    @staticmethod
    def solve(y: int, x: int, grid: list[list[int]]) -> int:
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
            grid = []
            for i, line in enumerate(file):
                if i == 0:
                    startY, startX = line.strip().split(' ')
                else:
                    grid.append(line.strip().split(', '))

        return int(startY), int(startX), grid
    
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

