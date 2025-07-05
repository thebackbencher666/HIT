import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HIT")

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

def load_high_score():
    try:
        with open("scores.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    high_score = load_high_score()
    if score > high_score:
        with open("scores.txt", "w") as f:
            f.write(str(score))

def show_end_screen(score):
    high_score = load_high_score()
    if score > high_score:
        save_high_score(score)
        high_score = score

    run = True
    while run:
        WIN.blit(SPACE, (0, 0))
        result_text = WINNER_FONT.render("Game Over", True, "white")
        score_text = HEALTH_FONT.render(f"Score: {score}", True, "white")
        high_text = HEALTH_FONT.render(f"High Score: {high_score}", True, "white")
        replay_text = HEALTH_FONT.render("1. Replay", True, "white")
        menu_text = HEALTH_FONT.render("2. Main Menu", True, "white")
        exit_text = HEALTH_FONT.render("3. Exit", True, "white")

        WIN.blit(result_text, (WIDTH//2 - result_text.get_width()//2, HEIGHT//4))
        WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - 60))
        WIN.blit(high_text, (WIDTH//2 - high_text.get_width()//2, HEIGHT//2 - 20))
        WIN.blit(replay_text, (WIDTH//2 - replay_text.get_width()//2, HEIGHT//2 + 40))
        WIN.blit(menu_text, (WIDTH//2 - menu_text.get_width()//2, HEIGHT//2 + 90))
        WIN.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, HEIGHT//2 + 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return
                elif event.key == pygame.K_2:
                    from .menu import show_main_menu
                    show_main_menu()
                    return
                elif event.key == pygame.K_3:
                    pygame.quit()
                    exit()
