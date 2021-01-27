import sys
from Board import *
import pygame

CELL_SIZE = 20
CELL_NUMBER = 30
SCREEN_SIZE = CELL_NUMBER * CELL_SIZE
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snek")
BG_COLOUR = pygame.Color('black')
pygame.init()
pygame.display.flip()


def main_menu():
    space = False
    while True:
        SCREEN.fill(BG_COLOUR)
        font = pygame.font.SysFont("arial", 20)
        start_text = font.render("PRESS SPACE TO START ", True, pygame.Color('red'))
        SCREEN.blit(start_text, (CELL_NUMBER * CELL_SIZE // 2 - 110, CELL_NUMBER * CELL_SIZE // 2 - 100))
        if space:
            game()
            space = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space = True

        pygame.display.update()
        CLOCK.tick(60)


def game():
    running = True
    board = Board()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    board.snake.set_direction(Vector2(-1, 0))
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    board.snake.set_direction(Vector2(1, 0))
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    board.snake.set_direction(Vector2(0, -1))
                else:
                    board.snake.set_direction(Vector2(0, 1))
            if not board.running:
                running = False
        SCREEN.fill(BG_COLOUR)
        board.update()
        board.draw()
        board.check_collision()
        pygame.display.update()
        CLOCK.tick(10)


if __name__ == "__main__":
    main_menu()
