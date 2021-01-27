from Food import *
from Snake import *


class Board:
    def __init__(self):
        self.running = True
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0

    def update(self):
        self.snake.move()
        self.fruit.draw_fruit()
        self.out_of_bounds()

    def draw(self):
        self.snake.draw_snake()
        self.show_score()

    def check_collision(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit = Fruit()
            self.snake.grow()
            self.score += 1

    def out_of_bounds(self):
        if not (0 <= self.snake.body[0].x <= CELL_NUMBER - 1) or not (0 <= self.snake.body[0].y <= CELL_NUMBER - 1):
            self.running = False
            print(self.score)
        for body in self.snake.body[1:]:
            if self.snake.body[0] == body:
                self.running = False
                print(self.score)

    def show_score(self):
        font = pygame.font.SysFont("arial", 20)
        scoretext = font.render("Score:{}".format(self.score), True, pygame.Color('red'))
        SCREEN.blit(scoretext, (CELL_NUMBER * CELL_SIZE // 2 - 20, 15))

