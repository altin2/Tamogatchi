import pygame

class test_button(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('eggStage1')
        self.rect = self.image.get_rect()
        self.rect.center = [100,100]