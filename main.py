import pygame
import math
import time
import ast
from datetime import datetime 
from Saver import *
from tamoAnim import *
OpenedAt = round(datetime.timestamp(datetime.now())/3600,2)
#ast.literal_eval(X) converts list to string 
global f #this is our save file. we need to make this global becuase we use it in functions.
f = open('Save.txt','r+')

pointer = egg()
evolution = 0

def assignattributes():
    attributes = loadattributes() #this is a list
    tamo.HP = attributes[0] # assings the loaded values to the tamogatchi
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
        currentEvo = egg(tamo.Age)
        return currentEvo,evolution
    
    elif state[0] == 'child':
        currentEvo = toddler()
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

evolution = tamoEvolution(pointer, evolution)[1]
temp_pointer = tamoEvolution(pointer,evolution)[0]

tamo = temp_pointer


assignattributes()
Timedifference = round(OpenedAt-tamo.LastOnline,2)
print(f'Last opened {Timedifference} hours ago')
tamo.away(Timedifference)
Quitgame = input("Quit game? ")

if Quitgame == 'yes':
    tamo.LastOnline = round(datetime.timestamp(datetime.now())/3600,2) # we need to change this right before the program closes.
    saveattributes(tamo)



#BELOW TO BE PUT IN MAIN WHILE LOOP

name = ''
keys = pygame.key.get_pressed()
char = pygame.key.name(event.key)

typing = False

if type_box.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed():
    typing = True

if typing:
    name = name + char
    if keys[pygame.K_BACKSPACE]:
        typing = False
        tamo.name = name
