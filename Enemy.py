import pygame
import random
import math

RED = (255, 0, 0)
WIDTH, HEIGHT = 800, 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, tick):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill(RED)  # Assicurati che siano visibili (rosso su sfondo nero)
        self.rect = self.image.get_rect()
        self.player = player  
        self.speed = 1.5
        self.tick = tick
        # Spawn appena fuori dai bordi per renderli subito visibili
        side = random.choice(["top", "bottom", "left", "right"])
        
        if side == "top":
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = -self.rect.height  
            
        elif side == "bottom":
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = HEIGHT  
            
        elif side == "left":
            self.rect.x = -self.rect.width 
            self.rect.y = random.randint(0, HEIGHT - self.rect.height)
            
        elif side == "right":
            self.rect.x = WIDTH 
            self.rect.y = random.randint(0, HEIGHT - self.rect.height)

        # DEBUG: Stampa in console la posizione iniziale
        print(side)

    def reset(self):
        self.speed = 1.5

    def update(self):
        # Calcola la direzione verso il player
        direction_playerx = self.player.rect.x - self.rect.x
        direction_playery = self.player.rect.y - self.rect.y
        distance = math.sqrt(direction_playerx**2 + direction_playery**2)
        self.speed = 1.5 + (self.tick / 1000)

        if distance != 0:
            self.rect.x += (direction_playerx / distance) * self.speed
            self.rect.y += (direction_playery / distance) * self.speed
        
        # Se il nemico esce completamente dallo schermo, viene eliminato
        if (self.rect.top > HEIGHT or self.rect.bottom < 0 or
            self.rect.left > WIDTH or self.rect.right < 0):
            self.kill()
