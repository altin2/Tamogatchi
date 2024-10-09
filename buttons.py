import pygame
import os
class feedbutton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\HungerBarMC.png')
        self.rect = self.image.get_rect()
        self.rect.center = [500,500]

    def action(self, tamo):
        tamo.feed(5)
        print(tamo.Hunger, ' ', tamo.weight)
class drinkbutton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\ThirstBar.png')
        self.rect = self.image.get_rect()
        self.rect.center = [350,500]

    def action(self, tamo):
        tamo.drink(5)
        print(tamo.Thirst)
class ScreenText(pygame.sprite.Sprite):
    def __init__(self,Text, center):
        pygame.sprite.Sprite.__init__(self)
        self.Text = Text
        self.center = center
        self.rect = self.Text.get_rect(center = self.center)


