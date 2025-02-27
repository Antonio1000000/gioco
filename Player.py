import pygame
import os.path

BLUE = (0, 0, 255)
WIDTH, HEIGHT = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image_up = pygame.image.load(os.path.join("sprite_Player", "Player_run_left.png")).convert_alpha()
        self.image_up = pygame.transform.scale(self.image_up, (32, 32))

        self.image_down = pygame.image.load(os.path.join("sprite_Player", "Player_run_right.png")).convert_alpha()
        self.image_down = pygame.transform.scale(self.image_down, (32, 32))

        self.image_left = pygame.image.load(os.path.join("sprite_Player", "player_run_left.png")).convert_alpha()
        self.image_left = pygame.transform.scale(self.image_left, (32, 32))

        self.image_right = pygame.image.load(os.path.join("sprite_Player", "Player_run_right.png")).convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (32, 32))
        self.image = self.image_up
        
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 60)
        self.speed = 4  # Velocità aumentata
        self.health = 10

    def reset(self):
        self.health = 10

    def update(self):

        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.image = self.image_left
    
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.image = self.image_right

        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
            self.image = self.image_left

        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
            self.image = self.image_right
            
        self.screen.blit(self.image, self.rect)
