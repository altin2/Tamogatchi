import pygame
import math
import time
import ast
from datetime import datetime 
from Saver import *
OpenedAt = datetime.now()
f = open('Save.txt','r+')
OrigionalNames = f.readline()
print('Flag 1')
newlist = ast.literal_eval(OrigionalNames)
print(newlist)
print(newlist[0])
f.close()

def tamoEvolution(tamo, evolution):

    currentEvo = None
    state = tamo.checkEvolve(evolution)
    carryInfo = tamo.carryOver()

    evolution == state[1]
    
    if state[0] == 'egg':
        currentEvo = egg()
        return currentEvo,evolution
    
    elif state[0] == 'child':
        currentEvo = child()
        return currentEvo,evolution
    
    elif state[0] == 'intelligent':
        #do stuff
        print('hi')

#evolution = tamoEvolution(pointer, evolution)[0]
#pointer = tamoEvolution(pointer,evolution)[1]