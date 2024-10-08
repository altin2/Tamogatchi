import pygame
import os

class test_button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('tamoImages\HungerBarMC.png')
        self.rect = self.image.get_rect()
        self.rect.center = [500,100]

    def action(self, tamo):
        tamo.feed(2)