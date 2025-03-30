import pygame  
import sys  
import copy  
import random  
import time  

pygame.init()  

# Game settings
scale = 15  
score = 0  
level = 1  # Start at level 1
FOOD_PER_LEVEL = 3  # Foods needed to level up
INITIAL_SPEED = 10  
speed = INITIAL_SPEED  

# Colors
BACKGROUND_TOP = (0, 0, 50)  
BACKGROUND_BOTTOM = (0, 0, 0)  
SNAKE_COLOR = (255, 137, 0)  
FOOD_COLOR = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  
SNAKE_HEAD = (255, 247, 0)  
FONT_COLOR = (255, 255, 255)  
DEFEAT_COLOR = (255, 0, 0)  

display = pygame.display.set_mode((500, 500))  
pygame.display.set_caption("Snake Game")  
clock = pygame.time.Clock()  

class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start  
        self.y = y_start  
        self.w = scale  
        self.h = scale  
        self.x_dir = 1  
        self.y_dir = 0  
        self.history = [[self.x, self.y]]  
        self.length = 1  

    def reset(self):
        # Center the snake on the grid
        self.x = (500 // (2 * scale)) * scale
        self.y = (500 // (2 * scale)) * scale
        self.x_dir = 1  
        self.y_dir = 0  
        self.history = [[self.x, self.y]]  
        self.length = 1  

    def show(self):
        for i in range(self.length):
            color = SNAKE_HEAD if i == 0 else SNAKE_COLOR
            pygame.draw.rect(display, color, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):
        head = self.history[0]
        return abs(head[0] - food_x) < scale and abs(head[1] - food_y) < scale

    def grow(self):
        self.length += 1
        self.history.append(copy.deepcopy(self.history[-1]))  

    def death(self):
        # Check self-collision
        head = self.history[0]
        return any(
            head[0] == seg[0] and head[1] == seg[1]
            for seg in self.history[1:]
        )

    def update(self):
        # Update body positions
        for i in range(self.length-1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i-1])
        # Move head
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

class Food:
    def new_location(self, snake):
        global food_x, food_y
        while True:
            # Generate within grid, avoiding walls
            food_x = random.randrange(1, (500 // scale) - 1) * scale
            food_y = random.randrange(1, (500 // scale) - 1) * scale
            # Check if position not on snake
            if not any(seg[0] == food_x and seg[1] == food_y for seg in snake.history):
                break

    def show(self):
        pygame.draw.rect(display, FOOD_COLOR, (food_x, food_y, scale, scale))  

def show_score():
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Score: {score}", True, FONT_COLOR)
    display.blit(text, (10, 10))  

def show_level():
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Level: {level}", True, FONT_COLOR)
    display.blit(text, (10, 30))  

def gameLoop():
    global score, level, speed, FOOD_COLOR

    # Center snake on grid
    start_x = (500 // (2 * scale)) * scale
    start_y = (500 // (2 * scale)) * scale
    snake = Snake(start_x, start_y)  
    food = Food()  
    food.new_location(snake)  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                # Handle direction changes
                if event.key in [pygame.K_UP, pygame.K_DOWN] and snake.y_dir == 0:
                    snake.y_dir = -1 if event.key == pygame.K_UP else 1
                    snake.x_dir = 0
                elif event.key in [pygame.K_LEFT, pygame.K_RIGHT] and snake.x_dir == 0:
                    snake.x_dir = -1 if event.key == pygame.K_LEFT else 1
                    snake.y_dir = 0

        # Update snake position
        snake.update()  

        # Check wall collision
        head = snake.history[0]
        wall_collision = (
            head[0] < 0 or head[0] >= 500 or
            head[1] < 0 or head[1] >= 500
        )

        # Check collisions
        if wall_collision or snake.death():
            # Game Over
            score = 0  
            level = 1  
            speed = INITIAL_SPEED  
            display.fill(DEFEAT_COLOR)  
            font = pygame.font.SysFont(None, 72)
            text = font.render("Game Over!", True, FONT_COLOR)
            display.blit(text, (100, 200))  
            pygame.display.update()  
            time.sleep(2)  
            snake.reset()  
            food.new_location(snake)  
            continue  

        # Draw background
        for y in range(500):
            color = (
                BACKGROUND_TOP[0] + (BACKGROUND_BOTTOM[0] - BACKGROUND_TOP[0]) * y / 500,
                BACKGROUND_TOP[1] + (BACKGROUND_BOTTOM[1] - BACKGROUND_TOP[1]) * y / 500,
                BACKGROUND_TOP[2] + (BACKGROUND_BOTTOM[2] - BACKGROUND_TOP[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))  

        # Check food eaten
        if snake.check_eaten():
            score += 1  
            snake.grow()  
            food.new_location(snake)  
            FOOD_COLOR = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  

            # Level up every FOOD_PER_LEVEL points
            if score % FOOD_PER_LEVEL == 0:
                level += 1
                speed += 1  # Increase speed

        # Draw elements
        snake.show()  
        food.show()  
        show_score()  
        show_level()  

        pygame.display.update()  
        clock.tick(speed)  

gameLoop()