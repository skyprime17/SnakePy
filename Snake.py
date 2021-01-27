import pygame
from Main import CELL_SIZE, CELL_NUMBER, SCREEN
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(CELL_NUMBER / 2, CELL_NUMBER / 2)]
        self._direction = Vector2(1, 0)

    def draw_snake(self):
        for body in self.body:
            x_pos = body.x * CELL_SIZE
            y_pos = body.y * CELL_SIZE
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, pygame.Color('green'), snake_rect)

    def move(self):
        if len(self.body) == 1:
            body_copy = self.body
            body_copy[0] = body_copy[0] + self._direction
            self.body = body_copy
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self._direction)
            self.body = body_copy[:]

    def set_direction(self, direction):
        self._direction = direction

    def grow(self):
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self._direction)
        self.body = body_copy[:]