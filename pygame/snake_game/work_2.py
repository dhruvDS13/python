import pygame
import time

# Initialize pygame
pygame.init()

# Set up window
screen_width = 540
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Grid size
grid_size = 9
cell_size = screen_width // grid_size

# Font
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Example Sudoku puzzle (0 means empty cell)
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Make a copy of the original grid to track initial user inputs
original_grid = [[grid[row][col] for col in range(grid_size)] for row in range(grid_size)]

# Function to display text on screen
def text_screen(text, color, x, y, size=55):
    screen_text = pygame.font.SysFont(None, size).render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# Function to draw the grid
def draw_grid():
    for i in range(grid_size + 1):
        line_width = 5 if i % 3 == 0 else 1
        pygame.draw.line(gameWindow, black, (i * cell_size, 0), (i * cell_size, screen_width), line_width)
        pygame.draw.line(gameWindow, black, (0, i * cell_size), (screen_width, i * cell_size), line_width)

# Function to draw numbers on the grid
def draw_numbers(grid):
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] != 0:
                # If the number is in the original grid (initial input), display it in black
                if original_grid[row][col] != 0:
                    text_screen(str(grid[row][col]), black, col * cell_size + 20, row * cell_size + 10)
                # Otherwise, display solver's numbers in blue
                else:
                    text_screen(str(grid[row][col]), blue, col * cell_size + 20, row * cell_size + 10)

# Function to check if the number is valid in the current grid
def valid(grid, num, pos):
    # Check row
    for i in range(grid_size):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(grid_size):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

# Function to solve the Sudoku grid using backtracking
def solve(grid):
    find = find_empty(grid)
    if not find:
        return True  # Puzzle solved
    else:
        row, col = find

    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            grid[row][col] = 0  # Backtrack

    return False

# Function to find an empty cell
def find_empty(grid):
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 0:
                return (i, j)  # Return row, col
    return None

# Function to handle input from the user
def input_num(pos):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                if event.key == pygame.K_2:
                    return 2
                if event.key == pygame.K_3:
                    return 3
                if event.key == pygame.K_4:
                    return 4
                if event.key == pygame.K_5:
                    return 5
                if event.key == pygame.K_6:
                    return 6
                if event.key == pygame.K_7:
                    return 7
                if event.key == pygame.K_8:
                    return 8
                if event.key == pygame.K_9:
                    return 9
                if event.key == pygame.K_0 or event.key == pygame.K_DELETE:
                    return 0

# Main game loop
def game_loop():
    exit_game = False
    selected = None  # Selected cell

    while not exit_game:
        gameWindow.fill(white)

        # Draw the grid and numbers
        draw_grid()
        draw_numbers(grid)

        # Solve button
        pygame.draw.rect(gameWindow, blue, [200, 550, 150, 40])
        text_screen("SOLVE", white, 230, 555, 35)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < 540:
                    row, col = y // cell_size, x // cell_size
                    selected = (row, col)
                elif 200 <= x <= 350 and 550 <= y <= 590:
                    solve(grid)  # Solve the Sudoku puzzle

            if event.type == pygame.KEYDOWN and selected:
                grid[selected[0]][selected[1]] = input_num(selected)
                original_grid[selected[0]][selected[1]] = grid[selected[0]][selected[1]]  # Update original grid

        pygame.display.update()

    pygame.quit()

# Start the game
game_loop()
