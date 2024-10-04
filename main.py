import pygame
import math
import time
import os
import pickle
from datetime import datetime 
from Saver import *
OpenedAt = datetime.now()
f = open('Save.txt','r+')
Names = ['Tom','Altin']
f.write(Names)
OrigionalNames = f.readline()


def tamoEvolution(tamo, evolution):

    currentEvo = None
    state = tamo.checkEvolve(evolution)
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
#pointer = tamoEvolution(pointer,evolution)[2]