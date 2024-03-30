import os

import pygame
from enum import Enum
from OMNIPIVE.Games.pong import Pong
from OMNIPIVE.Games.TicTacToe.main import main_menu


class GameState(Enum):
    MENU = 1
    TIC_TAC_TOE = 2
    PING_PONG = 3


BACKGROUND_COLOR = (32, 32, 32)
BUTTON_COLOR = (48, 48, 48)
TEXT_COLOR = (255, 255, 255)
FOCUSED_COLOR = (200, 200, 200)
FONT_SIZE = 48
WIDTH, HEIGHT = 1100, 700

# Center of the screen
center_x = WIDTH / 2
center_y = HEIGHT / 2

# Button dimensions
button_width = 300
button_height = 100
button_border_width = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def launch_tic_tac_toe():
    main_menu()


def launch_ping_pong():
    Pong.main()


def draw_menu(screen, font):
    """Draws the main menu with Tic Tac Toe and Pong buttons."""
    selected_option = 0

    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.MENU

        # Check if Pygame is initialized before rendering text
        if pygame.font.get_init():
            # Draw Tic Tac Toe button
            tic_tac_toe_rect = pygame.Rect(center_x - button_width / 2, center_y - button_height / 2 - 100, button_width, button_height)
            pygame.draw.rect(screen, BUTTON_COLOR if selected_option != 0 else FOCUSED_COLOR, tic_tac_toe_rect, button_border_width)
            tic_tac_toe_text = font.render("Tic Tac Toe", True, TEXT_COLOR)
            screen.blit(tic_tac_toe_text, (center_x - tic_tac_toe_text.get_width() / 2, center_y - tic_tac_toe_text.get_height() / 2 - 100))

            # Draw Pong button
            pong_rect = pygame.Rect(center_x - button_width / 2, center_y - button_height / 2 + 100, button_width, button_height)
            pygame.draw.rect(screen, BUTTON_COLOR if selected_option != 1 else FOCUSED_COLOR, pong_rect, button_border_width)
            pong_text = font.render("Pong", True, TEXT_COLOR)
            screen.blit(pong_text, (center_x - pong_text.get_width() / 2, center_y - pong_text.get_height() / 2 + 100))

            pygame.display.flip()

        else:
            pygame.font.init()
            font = pygame.font.SysFont("comicsans", FONT_SIZE)
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.MENU
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 2
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 2
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        return GameState.TIC_TAC_TOE
                    elif selected_option == 1:
                        return GameState.PING_PONG


def main():
    pygame.init()

    # Set window caption
    pygame.display.set_caption("Game Options")
    font = pygame.font.SysFont("comicsans", FONT_SIZE)  # Initialize font here
    current_state = GameState.MENU
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    while True:
        # Initialize the screen inside the loop to avoid errors when the display surface is closed

        if current_state == GameState.MENU:
            # del screen
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

            next_state = draw_menu(screen, font)  # Pass the screen and font variables
            if next_state != GameState.MENU:
                current_state = next_state
            else:
                pygame.display.quit()
                pygame.quit()
                break

        if current_state == GameState.TIC_TAC_TOE:
            launch_tic_tac_toe()
            # current_state = GameState.MENU
            del screen
            pygame.font.init()
            font = pygame.font.SysFont("comicsans", FONT_SIZE)
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            current_state = draw_menu(screen, font)
        elif current_state == GameState.PING_PONG:
            launch_ping_pong()
            # current_state = GameState.MENU
            del screen
            pygame.font.init()
            font = pygame.font.SysFont("comicsans", FONT_SIZE)
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            current_state = draw_menu(screen, font)


if __name__ == '__main__':
    main()
