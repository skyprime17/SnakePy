import pygame
from random import randint
from Main import CELL_SIZE, CELL_NUMBER, SCREEN
from pygame.math import Vector2


class Fruit:
    def __init__(self):
        self.x = randint(1, CELL_NUMBER - 1)
        self.y = randint(1, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(SCREEN, pygame.Color('red'), fruit_rect)
