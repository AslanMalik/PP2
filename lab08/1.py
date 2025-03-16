import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((1400, 1050))

x, y = screen.get_width() // 2, screen.get_height() // 2

running = True

clock = pygame.image.load("clock.png")
hour_arm = pygame.image.load("rightarm.png")
minute_arm = pygame.image.load("leftarm.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    current_hour = now.hour % 12  # 12-часовой формат
    current_minute = now.minute

    minute_angle = -current_minute * 6
    hour_angle = -current_hour * 30 - current_minute * 0.5  

    rotated_minute = pygame.transform.rotate(minute_arm, minute_angle)
    rotated_hour = pygame.transform.rotate(hour_arm, hour_angle)

    screen.fill((255, 255, 255))
    screen.blit(clock, (0, 0)) 
    screen.blit(rotated_hour, (x - rotated_hour.get_width() // 2, y - rotated_hour.get_height() // 2))
    screen.blit(rotated_minute, (x - rotated_minute.get_width() // 2, y - rotated_minute.get_height() // 2))

    pygame.display.flip()  
    pygame.time.delay(1000)