import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 480))

running = True
pause_cont = False
songs = ["france.mp3", "germany.mp3", "italy.mp3", "uk.mp3", "usa.mp3"]
current_song = 0
clock = pygame.time.Clock()

pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if current_song > 0:
                    current_song -= 1
                    pygame.mixer.music.load(songs[current_song])
                    pygame.mixer.music.play()

            if event.key == pygame.K_RIGHT:
                if current_song < len(songs)-1:
                    current_song += 1
                    pygame.mixer.music.load(songs[current_song])
                    pygame.mixer.music.play()

            if event.key == pygame.K_SPACE:
                if pause_cont:
                    pygame.mixer.music.unpause()
                    pause_cont = False
                else:
                    pause_cont = True
                    pygame.mixer.music.pause()

    screen.fill("white")
    pygame.display.flip()
    clock.tick(60)

        




    

