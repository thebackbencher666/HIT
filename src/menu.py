import pygame
import sys
from .scoreboard import WIDTH, HEIGHT, WIN, SPACE, HEALTH_FONT, WINNER_FONT

def show_main_menu():
    run = True
    while run:
        WIN.blit(SPACE, (0, 0))
        title_text = WINNER_FONT.render("HIT", True, "white")
        play_text = HEALTH_FONT.render("Press ENTER to Play", True, "white")
        exit_text = HEALTH_FONT.render("Press ESC to Exit", True, "white")

        WIN.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//3))
        WIN.blit(play_text, (WIDTH//2 - play_text.get_width()//2, HEIGHT//2 + 10))
        WIN.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT//2 + 60))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
