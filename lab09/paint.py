import pygame 
 
WIDTH, HEIGHT = 1200, 800
FPS = 90  

is_drawing = False  # Indicates whether drawing is active
brush_size = 2  # Default brush size
draw_color = 'blue'  # Default color
draw_mode = 'pen'  # Default mode (pen)

pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) 
pygame.display.set_caption('Paint') 
clock = pygame.time.Clock() 
screen.fill(pygame.Color('white'))  
font = pygame.font.SysFont('None', 60) 

last_mouse_pos = (0, 0)  # Fix: Initialize last mouse position

def draw_line(screen, start_pos, end_pos, width, color): 
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    A, B, C = y2 - y1, x1 - x2, x2 * y1 - x1 * y2
    
    if dx > dy:
        if x1 > x2: x1, x2, y1, y2 = x2, x1, y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, int(y)), width)
    else:
        if y1 > y2: x1, x2, y1, y2 = x2, x1, y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (int(x), y), width)

def draw_rectangle(screen, start_pos, end_pos, width, color): 
    x1, y1 = start_pos
    x2, y2 = end_pos
    rect_width, rect_height = abs(x1 - x2), abs(y1 - y2)
    pygame.draw.rect(screen, pygame.Color(color), pygame.Rect(min(x1, x2), min(y1, y2), rect_width, rect_height), width)

def draw_circle(screen, start_pos, end_pos, width, color): 
    x1, y1 = start_pos
    x2, y2 = end_pos
    center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
    radius = abs(x1 - x2) // 2
    pygame.draw.circle(screen, pygame.Color(color), (center_x, center_y), radius, width)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_r: draw_mode = 'rectangle'  
            elif event.key == pygame.K_c: draw_mode = 'circle'  
            elif event.key == pygame.K_p: draw_mode = 'pen'  
            elif event.key == pygame.K_e: draw_mode = 'erase'  
            elif event.key == pygame.K_q: screen.fill(pygame.Color('white'))  

            if event.key == pygame.K_1: draw_color = 'black'  
            elif event.key == pygame.K_2: draw_color = 'green'  
            elif event.key == pygame.K_3: draw_color = 'red'  
            elif event.key == pygame.K_4: draw_color = 'blue'  
            elif event.key == pygame.K_5: draw_color = 'yellow'  

        if event.type == pygame.MOUSEBUTTONDOWN:  
            is_drawing = True
            start_pos = event.pos  

        if event.type == pygame.MOUSEBUTTONUP:  
            if draw_mode == 'rectangle': draw_rectangle(screen, start_pos, event.pos, brush_size, draw_color)  
            elif draw_mode == 'circle': draw_circle(screen, start_pos, event.pos, brush_size, draw_color)  
            is_drawing = False  

        if event.type == pygame.MOUSEMOTION:  
            if is_drawing and draw_mode == 'pen': draw_line(screen, last_mouse_pos, event.pos, brush_size, draw_color)  
            elif is_drawing and draw_mode == 'erase': draw_line(screen, last_mouse_pos, event.pos, brush_size * 2, 'white')  
            last_mouse_pos = event.pos  

    pygame.display.flip()
    clock.tick(FPS)
