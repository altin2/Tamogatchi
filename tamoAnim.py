import pygame
from Saver import *

def toddlerPlay(tamo, iter):

    #needs to have a variable for each iterationnin main while loop

    age = tamo.carryOver()[0]
    intel = tamo.carryOver()[1]
    weight = tamo.carryOver()[2]
    if iter < 6:
        tamo.state = 1
    elif iter < 12:
        tamo.state = 2
    elif iter < 18:
        tamo.state = 3
    elif iter < 24:
        tamo.state = 4
    elif iter < 30:
        tamo.state = 5
    elif iter < 36:
        tamo.state = 6
    elif iter < 42:
        tamo.state = 5
    elif iter < 48:
        tamo.state = 4
    elif iter < 54:
        tamo.state = 3
    elif iter < 60:
        tamo.state = 2
    elif iter < 66:
        tamo.state = 1
        return True