import pygame
import time
import random
 
pygame.init()
 

yellow = (67,13,0,255)
black = (0, 0, 0)
green = (4,47,102)
blue = (242,180,103,255)
 
scrn_width = 600
scrn_height = 400
 
scrn = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    scrn.blit(value, [0, 0])
 
 
 
def ur_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(scrn, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    scrn.blit(mesg, [scrn_width / 6, scrn_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = scrn_width / 2
    y1 = scrn_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, scrn_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, scrn_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            scrn.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", yellow)
            score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= scrn_width or x1 < 0 or y1 >= scrn_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        scrn.fill(blue)
        pygame.draw.rect(scrn, green, [foodx, foody, snake_block, snake_block])
        snakemain = []
        snakemain.append(x1)
        snakemain.append(y1)
        snake_List.append(snakemain)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snakemain:
                game_close = True
 
        ur_snake(snake_block, snake_List)
        score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, scrn_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, scrn_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()