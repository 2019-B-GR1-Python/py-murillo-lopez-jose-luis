import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

goal = misc.face()
divisionY = 0
divisionX = 0

def getMinPrime(number, factor):
    if(number / factor == 1):
        return factor
    elif(number % factor == 0):
        return getMinPrime(number / factor, 2)
    else:
        return getMinPrime(number, factor + 1)

def isCompleted(puzzle):
    return np.array_equal(goal, puzzle)

def cutPuzzle(toCut):
    vertical_slices = np.split(toCut, divisionY)
    handler = 0
    pieces_slices = np.zeros([int(pieces), int(goal.shape[0] / divisionY), int(goal.shape[1] / divisionX), 3], dtype=int)
    for slice in vertical_slices:
        horizontal_slices = np.hsplit(slice, divisionX)
        for h_slice in horizontal_slices:
            pieces_slices[handler] = h_slice
            handler += 1
    return pieces_slices

def generatePuzzle(pieces):
    global divisionX
    global divisionY
    divisionY = getMinPrime(int(pieces), 2)
    divisionX = int(int(pieces) / divisionY)
    pieces_slices = cutPuzzle(goal)
    np.random.shuffle(pieces_slices)
    return rebuildPuzzle(pieces_slices)

def rebuildPuzzle(pieces_slices):
    puzzle = np.zeros([divisionY, int(goal.shape[0] / divisionY), goal.shape[1], 3], dtype=int)
    for i in range(1, divisionY + 1):
        puzzle[i - 1] = np.concatenate(pieces_slices[(i -1) * divisionX: i * divisionX], 1)
    puzzle_final = np.concatenate(puzzle, 0)
    return puzzle_final

def showPuzzle():
    plt.figure(1)
    plt.subplot(121)
    plt.imshow(puzzle)
    plt.subplot(122)
    plt.imshow(goal)
    plt.show()

def movement_menu():
    print("Seleccione a donde desea desplazar esta pieza:")
    print("1. Arriba")
    print("2. Abajo")
    print("3. Izquierda")
    print("4. Derecha")
    return int(input("Seleccione una opción: "))

def movement(piece, order):
    actual_puzzle = cutPuzzle(puzzle)
    if(order == 1):
        toMove = (piece - divisionX) % int(pieces)
    elif(order == 2):
        toMove = (piece + divisionX) % int(pieces)
    elif(order == 3):
        toMove = (piece - 1) % int(pieces)
    else:
        toMove = (piece + 1) % int(pieces)
    actual_puzzle[[toMove, piece]] = actual_puzzle[[piece,toMove]] 
    return rebuildPuzzle(actual_puzzle)


pieces = input("Ingrese el número de piezas: ")

puzzle = generatePuzzle(pieces)

while(not isCompleted(puzzle)):
    showPuzzle()
    selected_piece = input(f"Seleccione una pieza [1 - {pieces}]: ")
    selected_movement = movement_menu()
    puzzle = movement(int(selected_piece) - 1, selected_movement)

showPuzzle()
