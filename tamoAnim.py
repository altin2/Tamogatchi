import pygame
from Saver import *

pygame.init()
screen = pygame.display.set_mode([600,600])
frame = int((1/60)*1000)

# def toddlerPlay(tamo, iter):

#     #needs to have a variable for each iterationnin main while loop

#     age = tamo.carryOver()[0]
#     intel = tamo.carryOver()[1]
#     weight = tamo.carryOver()[2]
#     if iter < 6:
#         tamo.state = 1
#     elif iter < 12:
#         tamo.state = 2
#     elif iter < 18:
#         tamo.state = 3
#     elif iter < 24:
#         tamo.state = 4
#     elif iter < 30:
#         tamo.state = 5
#     elif iter < 36:
#         tamo.state = 6
#     elif iter < 42:
#         tamo.state = 5
#     elif iter < 48:
#         tamo.state = 4
#     elif iter < 54:
#         tamo.state = 3
#     elif iter < 60:
#         tamo.state = 2
#     elif iter < 66:
#         tamo.state = 1
#         return True

def toddlerPlay(tamo, iter):

    #needs to have a variable for each iterationnin main while loop

    age = tamo.carryOver()[0]
    intel = tamo.carryOver()[1]
    weight = tamo.carryOver()[2]
    if iter < 6:
        return 1
    elif iter < 12:
        return 2
    elif iter < 18:
        return 3
    elif iter < 24:
        return 4
    elif iter < 30:
        return 5
    elif iter < 36:
        return 6
    elif iter < 42:
        return 5
    elif iter < 48:
        return 4
    elif iter < 54:
        return 3
    elif iter < 60:
        return 2
    elif iter < 66:
        return 1
    else:
        return 0
    
def strongLift(tamo, iter):

    #needs to have a variable for each iterationnin main while loop

    age = tamo.carryOver()[0]
    intel = tamo.carryOver()[1]
    weight = tamo.carryOver()[2]
    if iter < 6:
        return 1
    elif iter < 12:
        return 2
    elif iter < 18:
        return 3
    elif iter < 24:
        return 4
    elif iter < 30:
        return 5
    elif iter < 36:
        return 6
    elif iter < 42:
        return 7
    elif iter < 48:
        return 8
    elif iter < 54:
        return 1

animIteration = 0
iteration = True

tod = toddler()
strong = strong1(10)
tod.updateState
strong.updateState

anims = pygame.sprite.Group()

anims.add(tod)
anims.add(strong)

while __name__ == '__main__':

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
    screen.fill((255,255,255))

    animIteration += 1
    if animIteration >=66:
        animIteration = 0
        iteration = not iteration

    if iteration:
        tod.updateState
    
    if not iteration:
        strong.updateState
    
    anims.draw(screen)

    pygame.display.update()
    pygame.time.wait(frame)
    