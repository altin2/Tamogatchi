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
font = pygame.font.Font('freesansbold.ttf', 25)
clock = pygame.time.Clock()
frame = int((1/60)*1000)

OpenedAt = round(datetime.timestamp(datetime.now())/3600,2)
buttons = pygame.sprite.Group()
tamogotchis = pygame.sprite.Group()
#ast.literal_eval(X) converts list to string 
global f #this is our save file. we need to make this global becuase we use it in functions.
f = open('Save.txt','r+')

pointer = egg()
evolution = 0

tamo = pointer

#tamo = egg()

def assignattributes():
    attributes = loadattributes() #this is a list
    currentType = None
    print(attributes)

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
    tamo.Temp = attributes[12]

def saveattributes(tamogat, evo):
    List1 = []
    f = open('Save.txt',"w")
    for i in range(13):
        List1.append(tamogat.getterAtt()[i])
    List1.append(evo)
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

    evolution_temp = state[1]
    
    if state[0] == 'egg':
        currentEvo = egg(age)
        tamogotchis.empty()
        tamogotchis.add(tamo)
        return currentEvo,evolution_temp
    
    elif state[0] == 'toddler':
        currentEvo = toddler(age,0)
        tamogotchis.empty()
        tamogotchis.add(tamo)
        return currentEvo,evolution_temp
    
    elif state[0] == 'intelligent':
        currentEvo = intelligent1(age, intel, weight, strength)
        tamogotchis.empty()
        tamogotchis.add(tamo)
        return currentEvo,evolution_temp
    
    elif state[0] == 'strong':
        currentEvo = strong1(age, intel, weight, strength)
        tamogotchis.empty()
        tamogotchis.add(tamo)
        return currentEvo, evolution_temp
    
    elif state[0] == 'balanced':
        currentEvo = balanced1(age, intel, weight, strength)
        tamogotchis.empty()
        tamogotchis.add(tamo)
        return currentEvo, evolution_temp


def forceEvolve(tamo, amt, button):
    
    global pressed

    if (pygame.mouse.get_pos()[0] > button.rect.topleft[0] and pygame.mouse.get_pos()[0] < button.rect.topright[0]):
        if (pygame.mouse.get_pos()[1] > button.rect.topleft[1] and pygame.mouse.get_pos()[1] < button.rect.bottomleft[1]):
            if not pygame.mouse.get_pressed()[0]:
                pressed = False

    if (pygame.mouse.get_pos()[0] > button.rect.topleft[0] and pygame.mouse.get_pos()[0] < button.rect.topright[0]):
        if (pygame.mouse.get_pos()[1] > button.rect.topleft[1] and pygame.mouse.get_pos()[1] < button.rect.bottomleft[1]):
            if not pressed and pygame.mouse.get_pressed()[0]:
                print('evooooooooooooooooooooooooooooooooooooooooooooooooooooo')
                tamo.Age += amt
                pressed == True

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

evolution = tamoEvolution(tamo, evolution)[1]
temp_pointer = tamoEvolution(tamo,evolution)[0]

tamo = temp_pointer
prev_evo = 0

assignattributes()
Timedifference = round(OpenedAt-tamo.LastOnline,2)
print(f'Last opened {Timedifference} hours ago')

print(tamo.name)
tamo.away(Timedifference) 
pressed = False
#BELOW TO BE PUT IN MAIN WHILE LOOP
name = ''
def isButtonPressed(button, isAnim, iter = None):
    global pressed
    if not pygame.mouse.get_pressed()[0]:
        pressed = False

    if not pressed:
        if (pygame.mouse.get_pos()[0] > button.rect.topleft[0] and pygame.mouse.get_pos()[0] < button.rect.topright[0]):
            if (pygame.mouse.get_pos()[1] > button.rect.topleft[1] and pygame.mouse.get_pos()[1] < button.rect.bottomleft[1]):
                if pygame.mouse.get_pressed()[0]:  
                    if isAnim:  
                        button.action(tamo, iter)
                        pressed = True
                        return True
                    else:
                        button.action(tamo, iter = None)
                        pressed = True
name = ''
pressed = False

animIteration = 0
    # set button = class of button
    # if not pressed:
    #     if (pygame.mouse.get_pos()[0] > button.rect.topleft[0] and pygame.mouse.get_pos()[0] < button.rect.topright[0]):
    #         if (pygame.mouse.get_pos()[1] > button.rect.topleft[1] and pygame.mouse.get_pos()[1] < button.rect.bottomleft[1]):
    #             if pygame.mouse.get_pressed()[0]:  
                        #pressed = True


#All buttons need ot be created outside of while loop otherwise it slows the program downh

Feedbutton = feedbutton()
Drinkbutton = drinkbutton()
Excerbutton = excerciseButton()
Washbutton = WashButton()
ForceEvobuttton = forceEvo()
HeatButton = heatButton()

buttons.add(Feedbutton)
buttons.add(Drinkbutton)
buttons.add(Excerbutton)
buttons.add(Washbutton)
buttons.add(ForceEvobuttton)
buttons.add(HeatButton)

tamogotchis.add(tamo)

# test_tod = toddler()
# tamogotchis.add(test_tod)

while True:

    print('current evo: ', evolution, '|prev evo', prev_evo)

    currentEvo = tamo.checkEvolve(evolution)
    #print(evolution)
    print(currentEvo)
    if tamo.checkdeath()  == True:
        print("Your tamo is dead.")
        tamo.resetstats()
        saveattributes(tamo,'egg')
        f.close()
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tamo.LastOnline = round(datetime.timestamp(datetime.now())/3600,2) # we need to change this right before the program closes.
            saveattributes(tamo, currentEvo)
            f.close()
            pygame.quit()
    screen.fill((255,255,255))      

    #testing animations

    # test_tod = toddler()
    

    # print('state', test_tod.state)
    # print(animIteration)

    #general tamo updates
    print(tamoEvolution(tamo,evolution))
    print('i linke ', tamoEvolution(tamo,evolution)[0])

    evolution = tamoEvolution(tamo, evolution)[1]
    temp_pointer = tamoEvolution(tamo,evolution)[0]

    if prev_evo != evolution:
        print('----------------------------------------')
        tamo = temp_pointer

    print('tamo is ', tamo)

    tamogotchis.update()

    if currentEvo[0] == 'toddler' or currentEvo[0] == 'egg':
        tamo.updateState()
        print('hi')
    
    if currentEvo[0] == 'egg':
        tamo.checkTemp(60)

    tamo.checkHunger(60)
    tamo.checkThirst(60)
    tamo.checkHygiene(60)
    tamo.checkAge(60)
    #tamo.checkEvolve

    if not pygame.mouse.get_pressed()[0]:
        pressed = False

    forceEvolve(tamo,2.5,ForceEvobuttton)

    HungerText = ScreenText(font.render(f'Hunger {round(tamo.Hunger,2)}', True, black),(100,50))
    ThirstText = ScreenText(font.render(f'Thirst {round(tamo.Thirst,2)}', True, black),(100,80))
    WeightText = ScreenText(font.render(f'Weight {round(tamo.weight,2)}', True, black),(100,110))
    AgeText = ScreenText(font.render(f'Age {round(tamo.Age,2)}', True, black),(100,140))
    HPText = ScreenText(font.render(f'HP {round(tamo.HP,2)}', True, black),(100,170))
    HygText = ScreenText(font.render(f'Hygiene {round(tamo.Hygiene,2)}', True, black),(100,200))
    IntText = ScreenText(font.render(f'Intelligence {round(tamo.Intellegence,2)}', True, black),(100,230))
    StrText = ScreenText(font.render(f'Strength {round(tamo.Strength,2)}', True, black),(100,260))
    HappText = ScreenText(font.render(f'Happiness {round(tamo.Happiness,2)}', True, black),(100,290))
    if currentEvo[0] == 'egg':
        TempText = ScreenText(font.render(f'Temperature {round(tamo.Temp,2)}', True, black),(100,320))
        screen.blit(TempText.Text,TempText.rect)
        isButtonPressed(HeatButton, False, None)
    #Showing text
    screen.blit(HungerText.Text,HungerText.rect)
    screen.blit(ThirstText.Text,ThirstText.rect)
    screen.blit(WeightText.Text,WeightText.rect)
    screen.blit(AgeText.Text,AgeText.rect)
    screen.blit(HPText.Text,HPText.rect)
    screen.blit(HygText.Text,HygText.rect)
    screen.blit(IntText.Text,IntText.rect)
    screen.blit(HappText.Text,HappText.rect)
    screen.blit(StrText.Text,StrText.rect)

    #Showing buttons
    isButtonPressed(Feedbutton, False, None)
    isButtonPressed(Drinkbutton, False, None)
    isButtonPressed(Excerbutton, True, animIteration)
    isButtonPressed(Washbutton, False, None)

    #if isButtonPressed(Excerbutton, True, animIteration):
    #test_tod.state = toddlerPlay(test_tod, animIteration)
    animIteration += 1
    if animIteration >=66:
        animIteration = 0
    # if tamo.checkEvolve == 'child':
    #     isButtonPressed(Excerbutton, True, animIteration)

    #     if isButtonPressed(Excerbutton, True, animIteration):
    #         animIteration += 1
    #         tamo.updateState()

    prev_evo = (evolution)

    tamogotchis.update()

    buttons.draw(screen)
    tamogotchis.draw(screen)
    pygame.display.update()

    pygame.time.wait(frame)