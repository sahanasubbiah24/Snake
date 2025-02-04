import pygame
import random


pygame.init()


WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (GRID_SIZE, 0)
        self.grow = False

    def move(self):

        head = self.body[0]


        new_head = (
            (head[0] + self.direction[0]) % WIDTH,
            (head[1] + self.direction[1]) % HEIGHT
        )


        self.body.insert(0, new_head)


        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, surface):
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

    def check_collision(self):

        head = self.body[0]
        return head in self.body[1:]


class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        x = random.randrange(0, WIDTH, GRID_SIZE)
        y = random.randrange(0, HEIGHT, GRID_SIZE)
        return (x, y)

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)


def main():

    snake = Snake()
    food = Food()


    score = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, GRID_SIZE):
                    snake.direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -GRID_SIZE):
                    snake.direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and snake.direction != (GRID_SIZE, 0):
                    snake.direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-GRID_SIZE, 0):
                    snake.direction = (GRID_SIZE, 0)


        snake.move()


        if snake.body[0] == food.position:
            snake.grow = True
            food.position = food.randomize_position()
            score += 1

        if snake.check_collision():
            running = False


        screen.fill(BLACK)


        snake.draw(screen)
        food.draw(screen)


        pygame.display.flip()


        clock.tick(10)


    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()


    pygame.time.wait(2000)



if __name__ == "__main__":
    main()
    pygame.quit()
