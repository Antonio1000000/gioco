import pygame
import random


RED = (255, 0, 0)
BOOST_WIDTH = 30
BOOST_HEIGHT = 30

class Boost(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, player):
        super().__init__()
        self.image = pygame.image.load("apple.png")  
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player = player
        self.respawn()

    def respawn(self):
        
        self.rect.x = random.randint(50, self.screen_width - 50)
        self.rect.y = random.randint(50, self.screen_height - 50)

    def update(self):
        
        if self.rect.colliderect(self.player.rect):  
            self.player.double_shot = True  
            self.player.boost_timer = pygame.time.get_ticks()  
            self.respawn()  
