import pygame

pygame.init()


height, weight = 480, 800

screen = pygame.display.set_mode((weight, height))

running = True

clock = pygame.time.Clock()
fps = 60
x, y = 400, 240
red = (255, 0, 0)
green = (0, 255, 0)

up, down, left, right = False, False, False, False
step = 20
radius = 40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
    

    if up and y - radius - step >= 0:
        y -= step
    if down and y + radius + step <= height:
        y += step
    if left and x - radius-step >= 0:
        x -= step
    if right and x + radius + step <= weight:
        x += step



    screen.fill(green)
    pygame.draw.circle(screen, red, (x, y), radius)
    pygame.display.flip()
    clock.tick(fps)

