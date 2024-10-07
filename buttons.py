import pygame
import os

class test_button(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('tamoImages\eggStage1.png')
        self.rect = self.image.get_rect()
        self.rect.center = [100,100]