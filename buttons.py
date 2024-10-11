import pygame
import os
from tamoAnim import *

class feedbutton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\HungerBarMC.png')
        self.rect = self.image.get_rect()
        self.rect.center = [600,75]

    def action(self, tamo,iter):
        tamo.feed(5)
        print(tamo.Hunger, ' ', tamo.weight)
        iter = None

class drinkbutton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\ThirstBar.png')
        self.rect = self.image.get_rect()
        self.rect.center = [450,75]

    def action(self, tamo,iter):
        tamo.drink(5)
        print(tamo.Thirst)
        iter = None

class WashButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\WashingButton.png')
        self.rect = self.image.get_rect()
        self.rect.center = [450,200]

    def action(self, tamo,iter):
        tamo.clean(5)
        print(tamo.Hygiene)
        iter = None

class excerciseButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\excerciseButton.png')
        self.rect = self.image.get_rect()
        self.rect.center = [350,75]

    def action(self,tamo, iter):
        tamo.state = toddlerPlay(tamo, iter)

class ScreenText(pygame.sprite.Sprite):
    def __init__(self,Text, center):
        pygame.sprite.Sprite.__init__(self)
        self.Text = Text
        self.center = center
        self.rect = self.Text.get_rect(center = self.center)

class forceEvo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\evoButton.png')
        self.rect = self.image.get_rect()
        self.rect.center = [600,600]


class heatButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\heatButton.png')
        self.rect = self.image.get_rect()
        self.rect.center = [600,200]

    def action(self, tamo, iter):
        print('yellow')
        tamo.Temp += 10
