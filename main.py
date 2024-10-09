import pygame
import math
import time
import ast
import sys
from datetime import datetime 
from Saver import *
from tamoAnim import *
from buttons import *
pygame.init()
# screen resolution
res = (680,680)
black = (0,0,0)
# opens up a window
screen = pygame.display.set_mode(res)
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
frame = int((1/60)*1000)

OpenedAt = round(datetime.timestamp(datetime.now())/3600,2)

#ast.literal_eval(X) converts list to string 
global f #this is our save file. we need to make this global becuase we use it in functions.
f = open('Save.txt','r+')

# pointer = egg()
# evolution = 0

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
    tamo.name = attributes[11]
def saveattributes(tamogat):
    List1 = []
    f = open('Save.txt',"w")
    for i in range(12):
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

# def displayAtts(tamo):
#     font = pygame.font.SysFont('Arial', 25)
#     attributes = tamo.getterAtt()
#     health = font.render(tamo.HP)
#     tamo.Hunger
#     tamo.Happiness
#     tamo.Thirst
#     tamo.Age
#     tamo.Intellegence
#     tamo.Hygiene
#     tamo.weight
#     tamo.Strength
#     tamo.LastOnline
#     tamo.Action
#     tamo.name


# evolution = tamoEvolution(pointer, evolution)[1]
# temp_pointer = tamoEvolution(pointer,evolution)[0]
tamo = Tamo()
# tamo = temp_pointer

assignattributes()
Timedifference = round(OpenedAt-tamo.LastOnline,2)
print(f'Last opened {Timedifference} hours ago')

print(tamo.name)
tamo.away(Timedifference) 
pressed = False
#BELOW TO BE PUT IN MAIN WHILE LOOP
name = ''
def isButtonPressed(button):
    global pressed
    if not pygame.mouse.get_pressed()[0]:
        pressed = False

    if not pressed:
        if (pygame.mouse.get_pos()[0] > button.rect.topleft[0] and pygame.mouse.get_pos()[0] < button.rect.topright[0]):
            if (pygame.mouse.get_pos()[1] > button.rect.topleft[1] and pygame.mouse.get_pos()[1] < button.rect.bottomleft[1]):
                if pygame.mouse.get_pressed()[0]:  
                    button.action(tamo)
                    pressed = True

name = ''
pressed = False

buttons = pygame.sprite.Group()
tamogotchis = pygame.sprite.Group()
animIteration = 0
    # set button = class of button
    # if not pressed:
    #     if (pygame.mouse.get_pos()[0] > button.rect.topleft[0] and pygame.mouse.get_pos()[0] < button.rect.topright[0]):
    #         if (pygame.mouse.get_pos()[1] > button.rect.topleft[1] and pygame.mouse.get_pos()[1] < button.rect.bottomleft[1]):
    #             if pygame.mouse.get_pressed()[0]:  
                        #pressed = True
count = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            tamo.LastOnline = round(datetime.timestamp(datetime.now())/3600,2) # we need to change this right before the program closes.
            saveattributes(tamo)
            pygame.quit()
    screen.fill((255,255,255))      

    #testing animations

    # test_tod = toddler()
    # tamogotchis.add(test_tod)
    # count += 1
    
    # if count == 120:
    #     toddlerPlay(test_tod, animIteration)

    #general tamo updates
    
    tamo.checkHunger(60)
    tamo.checkThirst(60)
    tamo.checkHygiene(60)
    tamo.checkAge(60)

    print(tamo.Hunger)
    print(tamo.Thirst)

    Feedbutton = feedbutton()
    Drinkbutton = drinkbutton()

    HungerText = ScreenText(font.render(f'Hunger {round(tamo.Hunger,2)}', True, black),(120,100))
    ThirstText = ScreenText(font.render(f'Thirst {round(tamo.Thirst,2)}', True, black),(120,150))
    WeightText = ScreenText(font.render(f'Weight {round(tamo.weight,2)}', True, black),(120,200))
    AgeText = ScreenText(font.render(f'Age {round(tamo.Age,2)}', True, black),(120,250))
    HPText = ScreenText(font.render(f'HP {round(tamo.HP,2)}', True, black),(120,300))

    buttons.add(Feedbutton)
    buttons.add(Drinkbutton)

    #Showing text
    screen.blit(HungerText.Text,HungerText.rect)
    screen.blit(ThirstText.Text,ThirstText.rect)
    screen.blit(WeightText.Text,WeightText.rect)
    screen.blit(AgeText.Text,AgeText.rect)
    screen.blit(HPText.Text,HPText.rect)
    #Showing buttons
    isButtonPressed(Feedbutton)
    isButtonPressed(Drinkbutton)

    # print(count)
    
    buttons.draw(screen)
    tamogotchis.draw(screen)
    pygame.display.update()

    pygame.time.wait(frame)