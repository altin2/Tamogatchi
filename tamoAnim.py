import pygame
from Saver import *

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode([600,600])
frame = int((1/60)*1000)

def toddlerPlay(tamo, iter):

    #needs to have a variable for each iterationnin main while loop
    
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

    #needs to have a variable for each iteration in main while loop

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

if __name__ == '__main__':
    animIteration = 0
    iteration = True

    tod = toddler(5)
    strong = strong1(10)

    tod.x_cord = 150
    tod.y_cord = 300

    strong.x_cord = 450
    strong.y_cord = 300

    tod.updateState()
    strong.updateState()

    anims = pygame.sprite.Group()

    anims.add(tod)
    anims.add(strong)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
        screen.fill((255,255,255))

        animIteration += 1
        if animIteration >=66:
            animIteration = 0
            iteration = not iteration

        if iteration:
            tod.state = toddlerPlay(tod,animIteration)
            tod.updateState()
        
        if not iteration:

            strong.state = strongLift(strong, animIteration)
            strong.updateState()
        
        print(animIteration)
        anims.draw(screen)

        pygame.display.update()
        pygame.time.wait(frame)
        