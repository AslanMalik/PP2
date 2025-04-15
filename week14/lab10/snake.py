
import pygame
import random
import psycopg2
from color_palette import *

pygame.init()

# Размеры экрана и ячейки
WIDTH, HEIGHT = 600, 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Шрифты
font = pygame.font.SysFont("Verdana", 20)

# Подключение и работа с базой данных
def get_user_data(username):
    conn = psycopg2.connect(
        dbname="suppliers", user="postgres", password="Python2006!", host="localhost", port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username=%s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
        cur.execute(
            "SELECT score, level FROM user_score WHERE user_id=%s ORDER BY created_at DESC LIMIT 1",
            (user_id,)
        )
        last_score = cur.fetchone()
        if last_score:
            score, level = last_score
        else:
            score, level = 0, 1
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        score, level = 0, 1

    conn.commit()
    cur.close()
    conn.close()
    return user_id, score, level

def save_user_state(user_id, score, level):
    conn = psycopg2.connect(
        dbname="suppliers", user="postgres", password="Python2006!", host="localhost", port="5432"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level)
    )
    conn.commit()
    cur.close()
    conn.close()

# Ввод имени пользователя и загрузка состояния
username = input("Введите ваше имя: ")
user_id, start_score, start_level = get_user_data(username)

# Функция отрисовки шахматной сетки
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(WIDTH // CELL):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(
                screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки на поле
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0
        self.score = start_score
        self.level = start_level
        self.speed = 5 + (self.level - 1)

    def move(self):
        new_x = self.body[0].x + self.dx
        new_y = self.body[0].y + self.dy

        if new_x < 0 or new_x >= WIDTH // CELL or new_y < 0 or new_y >= HEIGHT // CELL:
            return False

        if any(new_x == segment.x and new_y == segment.y for segment in self.body):
            return False

        self.body.insert(0, Point(new_x, new_y))
        self.body.pop()
        return True

    def grow(self, weight):
        tail = self.body[-1]
        for _ in range(weight):
            self.body.append(Point(tail.x, tail.y))
        self.score += weight
        if self.score % 3 == 0:
            self.level += 1
            self.speed += 1

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.grow(food.weight)
            return True
        return False

# Класс еды
class Food:
    def __init__(self, snake):
        self.generate_random_position(snake)
        self.weight = random.randint(1, 3)
        self.timer = pygame.time.get_ticks()

    def generate_random_position(self, snake):
        while True:
            self.pos = Point(random.randint(0, (WIDTH // CELL) - 1),
                             random.randint(0, (HEIGHT // CELL) - 1))
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break
        self.timer = pygame.time.get_ticks()

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
        weight_text = font.render(str(self.weight), True, colorBLACK)
        screen.blit(weight_text, (self.pos.x * CELL + 5, self.pos.y * CELL + 5))

# Инициализация объектов
snake = Snake()
food = Food(snake)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_user_state(user_id, snake.score, snake.level)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_p:
                save_user_state(user_id, snake.score, snake.level)
                paused = True
                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.KEYDOWN and pause_event.key == pygame.K_p:
                            paused = False

    draw_grid_chess()

    if not snake.move():
        save_user_state(user_id, snake.score, snake.level)
        running = False

    if snake.check_collision(food):
        food = Food(snake)

    if pygame.time.get_ticks() - food.timer > 5000:
        food = Food(snake)

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(snake.speed)

pygame.quit()