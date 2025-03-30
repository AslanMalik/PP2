import pygame 
import math  # Added for math operations

WIDTH, HEIGHT = 1200, 800
FPS = 90  
is_drawing = False  
brush_size = 2  
draw_color = 'blue'  
draw_mode = 'pen'  

pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) 
pygame.display.set_caption('Paint') 
clock = pygame.time.Clock() 
screen.fill(pygame.Color('white'))  
font = pygame.font.SysFont('None', 60) 
last_mouse_pos = (0, 0)  

def draw_line(screen, start_pos, end_pos, width, color): 
    """Draw a continuous line using circles between two points."""
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
    """Draw a rectangle from top-left to bottom-right."""
    x1, y1 = start_pos
    x2, y2 = end_pos
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    pygame.draw.rect(screen, pygame.Color(color), rect, width)

def draw_circle(screen, start_pos, end_pos, width, color): 
    """Draw a circle with center between start and end points."""
    x1, y1 = start_pos
    x2, y2 = end_pos
    center = ((x1 + x2) // 2, (y1 + y2) // 2)
    radius = int(math.hypot(x2 - x1, y2 - y1) // 2)
    pygame.draw.circle(screen, pygame.Color(color), center, radius, width)

def draw_square(screen, start_pos, end_pos, width, color):
    """Draw a square with equal width and height."""
    x1, y1 = start_pos
    x2, y2 = end_pos
    side = max(abs(x2 - x1), abs(y2 - y1))  # Use larger dimension for consistency
    # Adjust end position to maintain square shape
    x2 = x1 + side if x2 > x1 else x1 - side
    y2 = y1 + side if y2 > y1 else y1 - side
    rect = pygame.Rect(min(x1, x2), min(y1, y2), side, side)
    pygame.draw.rect(screen, pygame.Color(color), rect, width)

def draw_right_triangle(screen, start_pos, end_pos, width, color):
    """Draw a right-angled triangle with the right angle at the start position."""
    x1, y1 = start_pos
    x2, y2 = end_pos
    points = [(x1, y1), (x2, y1), (x1, y2)]  # Right angle at (x1,y1)
    pygame.draw.polygon(screen, pygame.Color(color), points, width)

def draw_equilateral_triangle(screen, start_pos, end_pos, width, color):
    """Draw an equilateral triangle with the base as start-end points."""
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    if length == 0: return
    height = (math.sqrt(3) / 2) * length  # Height of equilateral triangle
    # Calculate perpendicular direction
    perp_dx, perp_dy = -dy, dx  # Rotate 90 degrees
    # Normalize perpendicular vector
    perp_length = math.hypot(perp_dx, perp_dy)
    perp_dx /= perp_length
    perp_dy /= perp_length
    # Third point coordinates
    mid_x, mid_y = (x1 + x2)/2, (y1 + y2)/2
    third_x = mid_x + perp_dx * height
    third_y = mid_y + perp_dy * height
    points = [(x1, y1), (x2, y2), (third_x, third_y)]
    pygame.draw.polygon(screen, pygame.Color(color), points, width)

def draw_rhombus(screen, start_pos, end_pos, width, color):
    """Draw a rhombus inscribed in the rectangle defined by start and end points."""
    x1, y1 = start_pos
    x2, y2 = end_pos
    mid_x, mid_y = (x1 + x2)/2, (y1 + y2)/2
    points = [
        (mid_x, y1),  # Top
        (x2, mid_y),  # Right
        (mid_x, y2),  # Bottom
        (x1, mid_y)   # Left
    ]
    pygame.draw.polygon(screen, pygame.Color(color), points, width)

# Main loop
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()

        if event.type == pygame.KEYDOWN:  
            # Mode selection
            if event.key == pygame.K_r:   draw_mode = 'rectangle'
            elif event.key == pygame.K_c: draw_mode = 'circle'
            elif event.key == pygame.K_p: draw_mode = 'pen'
            elif event.key == pygame.K_e: draw_mode = 'erase'
            elif event.key == pygame.K_q: screen.fill(pygame.Color('white'))
            elif event.key == pygame.K_s: draw_mode = 'square'
            elif event.key == pygame.K_t: draw_mode = 'right_triangle'
            elif event.key == pygame.K_u: draw_mode = 'equilateral_triangle'
            elif event.key == pygame.K_h: draw_mode = 'rhombus'

            # Color selection
            if event.key == pygame.K_1:   draw_color = 'black'
            elif event.key == pygame.K_2: draw_color = 'green'
            elif event.key == pygame.K_3: draw_color = 'red'
            elif event.key == pygame.K_4: draw_color = 'blue'
            elif event.key == pygame.K_5: draw_color = 'yellow'

        # Drawing controls
        if event.type == pygame.MOUSEBUTTONDOWN:  
            is_drawing = True
            start_pos = event.pos  

        if event.type == pygame.MOUSEBUTTONUP:  
            # Finalize shape drawing
            if draw_mode == 'rectangle': 
                draw_rectangle(screen, start_pos, event.pos, brush_size, draw_color)
            elif draw_mode == 'circle': 
                draw_circle(screen, start_pos, event.pos, brush_size, draw_color)
            elif draw_mode == 'square': 
                draw_square(screen, start_pos, event.pos, brush_size, draw_color)
            elif draw_mode == 'right_triangle': 
                draw_right_triangle(screen, start_pos, event.pos, brush_size, draw_color)
            elif draw_mode == 'equilateral_triangle': 
                draw_equilateral_triangle(screen, start_pos, event.pos, brush_size, draw_color)
            elif draw_mode == 'rhombus': 
                draw_rhombus(screen, start_pos, event.pos, brush_size, draw_color)
            is_drawing = False  

        if event.type == pygame.MOUSEMOTION:  
            # Continuous drawing for pen/eraser
            if is_drawing and draw_mode == 'pen': 
                draw_line(screen, last_mouse_pos, event.pos, brush_size, draw_color)
            elif is_drawing and draw_mode == 'erase': 
                draw_line(screen, last_mouse_pos, event.pos, brush_size * 2, 'white')
            last_mouse_pos = event.pos  

    pygame.display.flip()
    clock.tick(FPS)