import pygame
import random

pygame.init()

snake_color = (255, 255, 255)
background_color = (0, 0, 0)
game_over_message_color = (255, 0, 0)
food_color = (255, 165, 0)
score_color = (75, 165, 235)

width, height = 1200, 800

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

snake_size = 25
snake_speed = 15

message_font = pygame.font.SysFont("ubuntu", 50)
score_font = pygame.font.SysFont("ubuntu", 40)

def print_score(score):
    score_text = score_font.render("Your score: " + str(score), True, score_color)
    game_display.blit(score_text, [0, 0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, snake_color, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():
    game_over = False
    game_closed = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_size) / 25.0) * 25.0
    food_y = round(random.randrange(0, height - snake_size) / 25.0) * 25.0

    while not game_closed:

        while game_over:
            game_display.fill(background_color)
            game_over_message = message_font.render("Game Over (Press 1 to restart, 2 to exit)", True, game_over_message_color)
            game_over_message_rectangle = game_over_message.get_rect(center=(width / 2, height / 2))
            game_display.blit(game_over_message, game_over_message_rectangle)
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        run_game()
                    if event.key == pygame.K_2:
                        pygame.quit()
                        quit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True
        
        x += x_speed
        y += y_speed

        game_display.fill(background_color)
        pygame.draw.rect(game_display, food_color, [food_x, food_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]
        
        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_over = True

        draw_snake(snake_size, snake_pixels)

        print_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 25.0) * 25.0
            food_y = round(random.randrange(0, height - snake_size) / 25.0) * 25.0
            snake_length += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()
