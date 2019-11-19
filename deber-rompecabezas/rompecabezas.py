import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

goal = misc.face()

def getMinPrime(number, factor):
    if(number / factor == 1):
        return factor
    elif(number % factor == 0):
        return getMinPrime(number / factor, 2)
    else:
        return getMinPrime(number, factor + 1)

def isCompleted(puzzle):
    return np.array_equal(goal, puzzle)

def generatePuzzle(pieces):
    divisionY = getMinPrime(int(pieces), 2)
    divisionX = int(int(pieces) / divisionY)
    vertical_slices = np.split(goal, divisionY)
    np.random.shuffle(vertical_slices)
    handler = 0
    pieces_slices = np.zeros([int(pieces), int(goal.shape[0] / divisionY), int(goal.shape[1] / divisionX), 3], dtype=int)
    for slice in vertical_slices:
        horizontal_slices = np.hsplit(slice, divisionX)
        for h_slice in horizontal_slices:
            pieces_slices[handler] = h_slice
            handler += 1
    np.random.shuffle(pieces_slices)
    return rebuildPuzzle(pieces_slices)

def rebuildPuzzle(pieces_slices):
    divisionY = getMinPrime(pieces_slices.shape[0], 2)
    divisionX = int(int(pieces) / divisionY)
    puzzle = np.zeros([divisionY, int(goal.shape[0] / divisionY), goal.shape[1], 3], dtype=int)
    for i in range(1, divisionY + 1):
        puzzle[i - 1] = np.concatenate(pieces_slices[(i -1) * divisionX: i * divisionX], 1)
    puzzle_final = np.concatenate(puzzle, 0)
    return puzzle_final

pieces = input("Ingrese el número de piezas: ")

puzzle = generatePuzzle(pieces)

#print(goal)

plt.imshow(puzzle)
plt.show()

puzzle = goal

print(isCompleted(puzzle))