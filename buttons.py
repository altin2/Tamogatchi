import pygame
import os
from tamoAnim import *

class feedbutton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\HungerBarMC.png')
        self.rect = self.image.get_rect()
        self.rect.center = [600,75]

    def action(self, tamo):
        tamo.feed(5)
        print(tamo.Hunger, ' ', tamo.weight)

class drinkbutton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\ThirstBar.png')
        self.rect = self.image.get_rect()
        self.rect.center = [450,75]

    def action(self, tamo):
        tamo.drink(5)
        print(tamo.Thirst)

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
