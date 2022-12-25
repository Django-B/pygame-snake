import pygame 
import random


WIDTH, HEIGHT = 400, 300
FPS = 10
SNAKE_SIZE = 10

# colors (R, G, B)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# other vars
X = WIDTH//2
Y = HEIGHT//2
snake_list = []
snake_length = 3

def init_pg():
    global screen, clock, text
    pygame.init() # create window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # font = pygame.font.Font(None, 20)
    # font = pygame.font.Font("Tahoma.ttf", 20)
    # text = font.render("Game over!", True, [255, 255, 255])

def draw_snake():
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, (x, y, SNAKE_SIZE, SNAKE_SIZE))

def draw_apple():
    pygame.draw.rect(screen, RED, (applex, appley, SNAKE_SIZE, SNAKE_SIZE))

def random_applexy() -> list:
    global applex, appley
    applex = round(random.randrange(0, WIDTH-SNAKE_SIZE) / 10)*10
    appley = round(random.randrange(0, HEIGHT-SNAKE_SIZE) / 10)*10
    return [applex, appley]

def game_cycle():
    global X, Y
    global x_change, y_change
    global snake_length
    x_change = 0
    y_change = 0

    random_applexy()

    running = True
    while running:
        clock.tick(FPS)
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # check for closing window
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                # game control
                elif event.key == pygame.K_a:
                    x_change = -SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_d:
                    x_change = SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_w:
                    y_change = -SNAKE_SIZE
                    x_change = 0
                elif event.key == pygame.K_s:
                    y_change = SNAKE_SIZE
                    x_change = 0

        # rendering
        screen.fill(BLACK)
        
        X += x_change
        Y += y_change

        snake_list.append([X, Y])

        if len(snake_list) > snake_length:
            del snake_list[0]

        draw_snake()
        draw_apple()

        # screen.blit(text, (10, 10))
        print(X, Y)

        if X == applex and Y == appley:
            snake_length += 1
            random_applexy()

        if X == WIDTH or Y == HEIGHT or X==-SNAKE_SIZE or Y==-SNAKE_SIZE:
            print('game over')
            running = False
        # update
        pygame.display.update()

init_pg()
game_cycle()
pygame.quit()
