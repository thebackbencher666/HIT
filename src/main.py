from .menu import show_main_menu
from .game import run_game
from .scoreboard import show_end_screen

def main():
    while True:
        show_main_menu()
        score = run_game()
        show_end_screen(score)

if __name__ == "__main__":
    main()
