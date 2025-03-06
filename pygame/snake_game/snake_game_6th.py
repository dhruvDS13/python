import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Creating window
screen_width = 800
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithDhruv")
pygame.display.update()

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# Function to display text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Function to plot the snake
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Function to draw boundaries
def draw_boundaries():
    pygame.draw.rect(gameWindow, black, [0, 40, screen_width, screen_height - 40], 5)  # Visible boundary

# Welcome screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to Snakes", black, 220, 200)
        text_screen("Press Space Bar To Play", black, 179, 245)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(30)

# Creating a game loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    init_velocity = 10
    score = 0
    snake_size = 10
    fps = 30

    # Food position (start below the header, which occupies the top 40 pixels)
    food_x = random.randint(20, screen_width - 40)
    food_y = random.randint(60, screen_height - 60)  # Starting from y = 60 to avoid the header

    # High score
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    
    with open("hiscore.txt", "r") as f:
        hiscore = f.read().strip()
        if not hiscore.isdigit():
            hiscore = 0
        else:
            hiscore = int(hiscore)

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen('''Game Over! Press Enter to continue''', red, 70, 180)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10
            
            snake_x += velocity_x
            snake_y += velocity_y

            # Snake eats food
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                print("Score: ", score)
                snk_length += 1
                if score > int(hiscore):
                    hiscore = score

                food_x = random.randint(20, screen_width - 40)
                food_y = random.randint(60, screen_height - 60)

            # Game screen and boundaries
            gameWindow.fill(white)
            draw_boundaries()
            text_screen("Score: " + str(score) + " Hiscore: " + str(hiscore), blue, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            # Game over conditions
            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 40 or snake_y > screen_height:
                game_over = True
                print("Game over")

            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

# Start the game
welcome()
