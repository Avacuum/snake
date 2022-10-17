import pygame
import random

from utils import generate_walls

WIDTH = 1280
HEIGHT = 720
FPS = 20

food_coordinates = [
    random.randint(1, 63) * 20,
    random.randint(1, 35) * 20
]
walls_amount = 20






print(walls)
input()
def generate_food_coordinates(width: int, height: int, walls: list, tile_size: int = 20):
    pass


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


pygame.font.init()
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

play_button = pygame.image.load('play_button.png')
rect = pygame.image.load('rect.png')

snake_speed_x = 20
snake_speed_y = 0
snake_x = 0
snake_y = 0
score = 0

running = True
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 100)
speed_base = 20
snake_list = []
Length_of_snake = 1
Game_over = False
Game_start = True
i = 0
pos = pygame.mouse.get_pos()
while running:

    clock.tick(FPS)
    prev_score = score
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snake_speed_x = -speed_base
                snake_speed_y = 0
            if event.key == pygame.K_d:
                snake_speed_x = speed_base
                snake_speed_y = 0
            if event.key == pygame.K_w:
                snake_speed_y = -speed_base
                snake_speed_x = 0
            if event.key == pygame.K_s:
                snake_speed_y = speed_base
                snake_speed_x = 0

            if event.key == pygame.K_LEFT and snake_speed_x != 20:
                snake_speed_x = -speed_base
                snake_speed_y = 0
            if event.key == pygame.K_RIGHT and snake_speed_x != -20:
                snake_speed_x = speed_base
                snake_speed_y = 0
            if event.key == pygame.K_UP and snake_speed_y != 20:
                snake_speed_y = -speed_base
                snake_speed_x = 0
            if event.key == pygame.K_DOWN and snake_speed_y != -20:
                snake_speed_y = speed_base
                snake_speed_x = 0

            if event.key == pygame.K_SPACE:
                Game_start = False
            if event.key == pygame.K_SPACE and Game_over:
                Game_start = True
                Game_over = False
                snake_x = 20
                snake_y = 20
                snake_speed_x = 20
                snake_speed_y = 0
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_1:
                screen.fill(WHITE)
                snake_speed_x = 0
                snake_speed_y = 0
                Game_over = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('x', pos[0])
            print('y', pos[1])

            if pos[0]>=357 and pos[0]<=841 and pos[1]>=245 and pos[1]<=451:
                Game_start = False



    if Game_start:
        screen.fill(WHITE)
        screen.blit(play_button, (300, 50))

    else:
        if snake_x < 0 or snake_y < 0 or snake_x > WIDTH - 20 or snake_y > HEIGHT - 20:
            Game_over = True

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if pressed[0]:
            pygame.draw.circle(screen, BLUE, pos, 5)
            pygame.display.update()

        if prev_score != score:
            print(score)

        if food_coordinates == [snake_x, snake_y]:
            Length_of_snake += 1
            score += 1
            food_coordinates = [
                random.randint(1, 63) * 20,
                random.randint(1, 35) * 20
            ]

        snake_x += snake_speed_x
        snake_y += snake_speed_y
        snake_Head = []
        snake_Head.append(snake_x)
        snake_Head.append(snake_y)
        if snake_Head in snake_list:
            Game_over = True
        else:
            snake_list.append(snake_Head)


        if snake_x == kor3 and snake_y == kor4:
            Game_over = True
        if snake_x == kor5 and snake_y == kor6:
            Game_over = True

        if snake_x == kor7 and snake_y == kor8:
            Game_over = True

        if snake_x == kor9 and snake_y == kor10:
            Game_over = True

        if len(snake_list) > Length_of_snake:
            del snake_list[0]
        screen.fill(WHITE)

        pygame.draw.rect(screen, RED, [food_coordinates[0], food_coordinates[1], 20, 20])
        print(food_coordinates)
        for x in snake_list:
            pygame.draw.rect(screen, GREEN, [x[0], x[1], 20, 20])
            pygame.draw.rect(screen, BLACK, (kor5, kor6, 20, 20))
            pygame.draw.rect(screen, BLACK, (kor7, kor8, 20, 20))
            pygame.draw.rect(screen, BLACK, (kor9, kor10, 20, 20))
        pygame.draw.rect(screen, BLACK, (kor3, kor4, 20, 20))


        text1 = f1.render(str(score), True, BLACK)
        screen.blit(text1, (1250, 10))
        if Game_over:
            screen.fill(BLACK)
            text2 = f2.render("Вы проиграли", True, WHITE)
            screen.blit(text2, (400, 350))
            Length_of_snake = 1
            score = 0
            snake_list = []


        if score == 100:
            screen.fill(YELLOW)
            text2 = f2.render("Вы победили", True, WHITE)
            screen.blit(text2, (400, 350))
        print(snake_x,snake_y)
    pygame.display.flip()
