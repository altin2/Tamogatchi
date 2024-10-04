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
    List = [tamogat.getterAtt()]
    f.write(List)
x = f.readline()
newlist = ast.literal_eval(x)
print(newlist[0]+newlist[1])
def tamoEvolution(tamo, evolution):

    currentEvo = None
    state = tamo.checkEvolve(evolution)
    age = tamo.carryOver()[0]
    intel = tamo.carryOver()[1]
    weight = tamo.carryOver()[2]
    strength = tamo.carryOver()[3]

    evolution == state[1]
    
    if state[0] == 'egg':
        currentEvo = egg()
        return currentEvo,evolution
    
    elif state[0] == 'child':
        currentEvo = child()
        return currentEvo,evolution
    
    elif state[0] == 'intelligent':
        currentEvo = intelligent1(age, intel, weight, strength)
        return currentEvo,evolution
    
    elif state[0] == 'strong':
        currentEvo = strong1(age, intel, weight, strength)
        return currentEvo, evolution
    
    elif state[0] == 'balanced':
        currentEvo = balanced1(age, intel, weight, strength)
        return currentEvo, evolution

#evolution = tamoEvolution(pointer, evolution)[1]
#pointer = tamoEvolution(pointer,evolution)[2]]
