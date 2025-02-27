import pygame
import math

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
WIDTH, HEIGHT = 800, 600

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_enemy):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7
        
        
        # Se c'è un nemico target, direziona il proiettile verso di lui
        if target_enemy:
            direction_x = target_enemy.rect.centerx - x
            direction_y = target_enemy.rect.centery - y
            distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
            
            # Direzione normalizzata
            self.dir_x = (direction_x / distance)
            self.dir_y = (direction_y / distance)
        

    def update(self):

        # Muove il proiettile in linea retta
        self.rect.x += self.dir_x * self.speed
        self.rect.y += self.dir_y * self.speed
        
        # Rimuove il proiettile se esce dallo schermo
        if (self.rect.bottom < 0 or self.rect.top > HEIGHT or
            self.rect.right < 0 or self.rect.left > WIDTH):
            self.kill()
