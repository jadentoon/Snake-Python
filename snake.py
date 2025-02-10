import pygame
import time
import random

speed = 12.5
x_axis = 400
y_axis = 400

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

pygame.init()

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((x_axis, y_axis))

fps = pygame.time.Clock()

snake_position = [100,40]
snake_body = [[100,40], [80,40], [60,40], [40,40]]

fruit_pos = [random.randrange(1, (x_axis//20)) *20, random.randrange(1, (y_axis//20)) *20]

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' +str(score), True, color)

    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    font = pygame.font.SysFont('times new roman', 25)
    game_over_surface = font.render('Your Score is : ' +str(score), True, red)

    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (x_axis/2, y_axis/4)

    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    pygame.quit()

    quit()



while True:

    fruit_spawn = True
    pause = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    if direction == 'UP':
        snake_position[1] -= 20
    if direction == 'DOWN':
        snake_position[1] += 20
    if direction == 'LEFT':
        snake_position[0] -= 20
    if direction == 'RIGHT':
        snake_position[0] += 20
    
    snake_body.insert(0, list(snake_position))

    if snake_position[0] == fruit_pos[0] and snake_position[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (x_axis//20)) *20, random.randrange(1, (y_axis//20)) *20]
    
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 20, 20))

    pygame.draw.rect(game_window, red, pygame.Rect(fruit_pos[0], fruit_pos[1], 20, 20))

    if snake_position[0] < 0 or snake_position[0] > x_axis - 10 or snake_position[1] < 0 or snake_position[1] > y_axis - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
        
    show_score(1, white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(speed)


