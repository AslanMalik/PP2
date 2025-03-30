# Importing required libraries
import pygame, sys
from pygame.locals import *
import random, time

# Initializing Pygame
pygame.init()

# Initializing Pygame Mixer for sounds
pygame.mixer.init()

# Load background music and set volume
pygame.mixer.music.load("background.wav")  # Background music file
pygame.mixer.music.set_volume(0.5)  # Set volume (0.0 - 1.0)
pygame.mixer.music.play(-1)  # Play music in an infinite loop

# Load crash sound effect
crash_sound = pygame.mixer.Sound("crash.wav")
crash_sound.set_volume(0.9)  # Set crash sound volume

# Frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

# Defining colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3  # Initial enemy speed
SCORE = 0  # Number of avoided enemies
COINS = 0  # Number of collected coins
ENEMY_SPEED_INTERVAL = 10  # Number of coins required to increase enemy speed
next_speed_increase = ENEMY_SPEED_INTERVAL  # Tracks next threshold for speed increase

# Setting up fonts
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create game screen
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")

# Enemy class (AI car)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Movement speed depends on global SPEED
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Coin class with different types and weights
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Define coin types with image, value, and spawn weight
        self.types = [
            {"image": "bronze_coin.png", "value": 1, "weight": 70},  # 70% chance
            {"image": "silver_coin.png", "value": 2, "weight": 20},  # 20% chance
            {"image": "gold_coin.png", "value": 5, "weight": 10},    # 10% chance
        ]
        self.respawn()  # Initialize the first coin

    def respawn(self):
        # Select coin type based on weighted probability
        total_weight = sum(t["weight"] for t in self.types)
        rand = random.randint(1, total_weight)
        current_weight = 0
        for coin_type in self.types:
            current_weight += coin_type["weight"]
            if rand <= current_weight:
                self.type = coin_type
                break
        # Load image and set value
        self.image = pygame.image.load(self.type["image"])
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        # Random position avoiding edges
        self.rect.center = (random.randint(40, SCREEN_WIDTH -40), random.randint(40, SCREEN_HEIGHT -40))
        self.last_collected = time.time()
        self.value = self.type["value"]  # Store the coin's value

    def move(self):
        # Respawn coin after 1.5 seconds if not collected
        current_time = time.time()
        if current_time - self.last_collected > 1.5:
            self.respawn()

# Player class (user-controlled car)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

# Create player, enemy, and coin objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Speed increase event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Function to display game over screen
def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (100, 250))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:  # Restart game on spacebar
                    return True
                elif event.key == K_ESCAPE:  # Exit game on ESC
                    return False

# Handle collision with enemy
def handle_collision():
    global SPEED, COINS, next_speed_increase
    crash_sound.play()  # Play crash sound
    SPEED = 3  # Reset speed
    COINS = 0  # Reset coins
    next_speed_increase = ENEMY_SPEED_INTERVAL  # Reset speed increase threshold
    return game_over_screen()

# Background scrolling variable
background_y = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Check for player collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        if not handle_collision():
            pygame.quit()
            sys.exit()

    # Scroll background
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Display score and collected coins
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(score_text, (10, 10))

    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(coin_text, (310, 10))

    # Move sprites and check for coin collection
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

        if entity == C1 and pygame.sprite.spritecollideany(P1, coins):
            COINS += C1.value  # Add coin's value to total
            # Check if collected enough coins to increase enemy speed
            if COINS >= next_speed_increase:
                SPEED += 1  # Increase enemy speed
                next_speed_increase += ENEMY_SPEED_INTERVAL  # Set next threshold
            C1.respawn()  # Respawn a new coin
        else:
            entity.move()

    pygame.display.update()
    FramePerSec.tick(FPS)