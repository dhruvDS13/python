import pygame
import random

x= pygame.init()

#colors
white = (255,255,255)
red =  (255,0,0)
black = (0,0,0)
blue= (0,0,255)

#Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#Game Title
pygame.display.set_caption("SnakesWithDhruv")
pygame.display.update()

#Game specific variable
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

init_velocity = 10
score = 0
snake_size = 10
fps = 30

food_x = random.randint(20, screen_width//3)
food_y = random.randint(20,screen_height//3)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text =font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y]) # blit is use to update you work on screen

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x, y, snake_size, snake_size])


snk_list = []
snk_length = 1

#Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               velocity_x = init_velocity
               velocity_y = 0
            
            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    
# snake aur food ke bich ke distance ko kam kerne se snake food eat karega 10 wahi represent ker raha hai
    if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
        score += 1
        print("Score: " , score*10) # show in console
        snk_length +=1
#//3 lagane se food borders pe nahi jayega
        food_x = random.randint(20, screen_width//3)
        food_y = random.randint(20,screen_height//3)
    
#game screen white rahege
    gameWindow.fill(white)
    text_screen("Score: " + str(score*10), blue,5,5)
    pygame.draw.rect(gameWindow,red,[food_x, food_y, snake_size, snake_size]) #snake food color

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]


    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()