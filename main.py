import pygame
import math
import time
import ast
from datetime import datetime 
from Saver import *
OpenedAt = datetime.now()
#ast.literal_eval(X) converts list to string 
f = open('Save.txt','r+')
List = []
def saveattributes(tamogat):
    List = []
x = f.readline()
newlist = ast.literal_eval(x)
print(newlist[0]+newlist[1])
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

#evolution = tamoEvolution(pointer, evolution)[1]
#pointer = tamoEvolution(pointer,evolution)[2]]
