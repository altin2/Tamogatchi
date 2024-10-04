import pygame
import math
import time
import ast
from datetime import datetime 
from Saver import *
OpenedAt = round(datetime.timestamp(datetime.now())/3600,2)
#ast.literal_eval(X) converts list to string 
global f
f = open('Save.txt','r+')
def assignattributes():
    attributes = loadattributes()
    tamo.HP = attributes[0]
    tamo.Hunger = attributes[1]
    tamo.Happiness =attributes[2]
    tamo.Thirst = attributes[3]
    tamo.Age = attributes[4]
    tamo.Intellegence = attributes[5]
    tamo.Hygiene = attributes[6]
    tamo.weight = attributes[7]
    tamo.Strength = attributes[8]
    tamo.LastOnline = attributes[9]
    tamo.Action = attributes[10]
def saveattributes(tamogat):
    List1 = []
    f = open('Save.txt',"w")
    for i in range(11):
        List1.append(tamogat.getterAtt()[i])
    f.write(str(List1))
def loadattributes():
    f = open('Save.txt',"r")
    YYY = f.readline()
    Printing = ast.literal_eval(YYY)
    return Printing
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
assignattributes()
tamo.feed(20)
Quitgame = input("Quit game? ")
Timedifference = round(OpenedAt-tamo.LastOnline,2)
print(f'Last opened {Timedifference} hours ago')
if Quitgame == 'yes':
    tamo.LastOnline = round(datetime.timestamp(datetime.now())/3600,2)
    saveattributes(tamo)