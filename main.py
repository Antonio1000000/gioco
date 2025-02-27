import pygame
import sys
import Enemy
import Bullet
import Player

pygame.init()
pygame.joystick.init()

WIDTH, HEIGHT = 800,600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
NUM_ENEMIES_LVL1 = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
tick = 0 
pygame.display.set_caption("Livello 1: Combatti i nemici!")
clock = pygame.time.Clock()
running = True
background = pygame.transform.scale(pygame.image.load("background-1.png"), (2000, 2000))

all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# Creiamo il player
player = Player.Player(screen) 
all_sprites.add(player)

# Creiamo i nemici
for _ in range(NUM_ENEMIES_LVL1):
    enemy = Enemy.Enemy(player, tick)
    all_sprites.add(enemy)
    enemy_group.add(enemy)

score = 0 
shoot_delay = 500  # Millisecondi tra uno sparo e l'altro quando si tiene premuto
last_shot = pygame.time.get_ticks()  # Tempo dell'ultimo sparo


while running:
    tick += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                bullet = Bullet.Bullet(player.rect.centerx, player.rect.top, enemy)
                all_sprites.add(bullet)
                bullet_group.add(bullet)

    # Update delle sprite
    all_sprites.update()

    # Collisioni tra proiettili e nemici
    hits = pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
    for hit in hits:
        score += 10
        enemy = Enemy.Enemy(player, tick)
        all_sprites.add(enemy)
        enemy_group.add(enemy)

    # Collisioni tra player e nemici
    hits = pygame.sprite.spritecollide(player, enemy_group, True)
    for hit in hits:
        player.health -= 1
        enemy = Enemy.Enemy(player, tick)
        all_sprites.add(enemy)
        enemy_group.add(enemy)
        if player.health <= 0:
            running = False

    # Disegno delle sprite
    screen.fill(BLACK)
    screen.blit(background, (-500, -500))
    all_sprites.draw(screen)
    
    # Visualizzazione punteggio e vite
    font = pygame.font.SysFont("Arial", 20)
    score_text = font.render(f"Punteggio: {score}", True, WHITE)
    health_text = font.render(f"Vite: {player.health}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 40))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
