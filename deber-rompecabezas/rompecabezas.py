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
    handler = 0
    pieces_slices = np.empty([int(pieces), int(goal.shape[0] / divisionY), int(goal.shape[1] / divisionX), 3])
    for slice in vertical_slices:
        horizontal_slices = np.hsplit(slice, divisionX)
        for h_slice in horizontal_slices:
            pieces_slices[handler] = h_slice
            handler += 1
    np.random.shuffle(pieces_slices)
    puzzle_1 = pieces_slices[0]
    for i in range(1,divisionX):
        puzzle_1 = np.concatenate((puzzle_1, pieces_slices[i]),1)
    puzzle_2 = pieces_slices[divisionX]
    for i in range(divisionX + 1, int(pieces)):
        puzzle_2 = np.concatenate((puzzle_2, pieces_slices[i]),1)
    puzzle = np.concatenate((puzzle_1, puzzle_2), 0)
    return puzzle


pieces = input("Ingrese el número de piezas: ")

puzzle = generatePuzzle(pieces)

#print(goal)

plt.imshow(puzzle)
plt.show()

puzzle = goal

print(isCompleted(puzzle))