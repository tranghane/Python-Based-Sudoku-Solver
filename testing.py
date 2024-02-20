# GUI.py
import pygame
from dokusan import generators
import numpy as np
pygame.font.init()

#generating soduku
arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))

newBoard = arr.reshape(9, 9)

newBoard = [[int(num) for num in row] for row in newBoard]

for i in range(len(newBoard)):
    for j in range(len(newBoard)):
        print(newBoard[i][j] + 1)