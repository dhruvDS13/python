import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Draw the game board
def draw_lines():
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, HEIGHT), LINE_WIDTH)

# Create the board
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Draw X or O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLUE, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, BLUE, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

# Check for a win
def check_win(player):
    for row in range(BOARD_ROWS):
        if all([cell == player for cell in board[row]]):  # Check rows
            return True
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):  # Check diagonal
        return True
    if all([board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)]):  # Check anti-diagonal
        return True
    return False

# Check for a tie
def check_tie():
    return all([cell is not None for row in board for cell in row])

# Main game loop
def main():
    screen.fill(WHITE)
    draw_lines()
    player = 'X'
    game_over = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = player
                    draw_figures()

                    if check_win(player):
                        print(f"Player {player} wins!")
                        game_over = True

                    if check_tie():
                        print("It's a tie!")
                        game_over = True

                    player = 'O' if player == 'X' else 'X'  # Switch player

        pygame.display.update()

if __name__ == "__main__":
    main()
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FONT_COLOR = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Draw the game board
def draw_lines():
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, HEIGHT), LINE_WIDTH)

# Create the board
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Draw X or O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLUE, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, BLUE, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

# Check for a win
def check_win(player):
    for row in range(BOARD_ROWS):
        if all([cell == player for cell in board[row]]):  # Check rows
            return True
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(BOARD_ROWS)]):  # Check diagonal
        return True
    if all([board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)]):  # Check anti-diagonal
        return True
    return False

# Check for a tie
def check_tie():
    return all([cell is not None for row in board for cell in row])

# Draw the result message
def draw_result(message):
    font = pygame.font.SysFont("comicsans", 30)
    text = font.render(message, True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

# Reset the board
def reset_board():
    global board, game_over, player
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    game_over = False
    player = 'X'
    screen.fill(WHITE)
    draw_lines()

# Main game loop
def main():
    global player, game_over, player1_name, player2_name
    screen.fill(WHITE)

    # Get player names
    player1_name = get_player_name(1)
    player2_name = get_player_name(2)

    draw_lines()
    player = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = player
                    draw_figures()

                    if check_win(player):
                        winner = player1_name if player == 'X' else player2_name
                        draw_result(f"{winner} wins!")
                        game_over = True

                    if check_tie():
                        draw_result("It's a tie!")
                        game_over = True

                    player = 'O' if player == 'X' else 'X'  # Switch player

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press R to reset the game
                    reset_board()

        draw_lines()
        draw_figures()
        pygame.display.update()

def get_player_name(player_number):
    font = pygame.font.SysFont("comicsans", 30)
    input_box = pygame.Rect(50, 100 + (player_number - 1) * 50, 200, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = True
    text = ''
    
    # Prompt for player name
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)
        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()

if __name__ == "__main__":
    main()
