import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = HEIGHT // ROWS

# Colors
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)
RED = (255, 0, 0)

# Load piece images
piece_images = {
    'king': pygame.image.load('king_image.png'),
    'queen': pygame.image.load('queen_image.png'),
    'rook': pygame.image.load('rook_image.png'),
    'bishop': pygame.image.load('bishop_image.png'),
    'knight': pygame.image.load('knight_image.png'),
    'pawn': pygame.image.load('pawn_image.png')
}

# Resize images
for piece_type, image in piece_images.items():
    piece_images[piece_type] = pygame.transform.scale(image, (SQUARE_SIZE // 2, SQUARE_SIZE // 2))

# Piece classes
class Piece:
    def __init__(self, row, col, color, piece_type):
        self.row = row
        self.col = col
        self.color = color
        self.piece_type = piece_type

    def move(self, row, col):
        self.row = row
        self.col = col

# Initialize pieces
pieces = []
for row in range(ROWS):
    for col in range(COLS):
        if row == 1:
            pieces.append(Piece(row, col, 'white', 'pawn'))
        elif row == 6:
            pieces.append(Piece(row, col, 'black', 'pawn'))
        elif row == 0:
            if col in [0, 7]:
                pieces.append(Piece(row, col, 'white', 'rook'))
            elif col in [1, 6]:
                pieces.append(Piece(row, col, 'white', 'knight'))
            elif col in [2, 5]:
                pieces.append(Piece(row, col, 'white', 'bishop'))
            elif col == 3:
                pieces.append(Piece(row, col, 'white', 'queen'))
            elif col == 4:
                pieces.append(Piece(row, col, 'white', 'king'))
        elif row == 7:
            if col in [0, 7]:
                pieces.append(Piece(row, col, 'black', 'rook'))
            elif col in [1, 6]:
                pieces.append(Piece(row, col, 'black', 'knight'))
            elif col in [2, 5]:
                pieces.append(Piece(row, col, 'black', 'bishop'))
            elif col == 3:
                pieces.append(Piece(row, col, 'black', 'queen'))
            elif col == 4:
                pieces.append(Piece(row, col, 'black', 'king'))

# Game variables
selected_piece = None

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fluffy Chess Game')

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Function to draw the board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to draw pieces
def draw_pieces():
    for piece in pieces:
        if piece.color == 'white':
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        
        # Draw piece image
        image = piece_images[piece.piece_type]
        screen.blit(image, (piece.col * SQUARE_SIZE + SQUARE_SIZE // 4, piece.row * SQUARE_SIZE + SQUARE_SIZE // 4))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row = event.pos[1] // SQUARE_SIZE
            col = event.pos[0] // SQUARE_SIZE
            
            # Select a piece
            if selected_piece is None:
                for piece in pieces:
                    if piece.row == row and piece.col == col:
                        selected_piece = piece
                        break
            # Move the selected piece
            else:
                # Basic move validation (no collision detection or rules)
                for piece in pieces:
                    if piece.row == row and piece.col == col:
                        break
                else:
                    selected_piece.move(row, col)
                selected_piece = None

    # Draw everything
    draw_board()
    draw_pieces()
    
    # Highlight selected piece
    if selected_piece:
        pygame.draw.rect(screen, RED, (selected_piece.col * SQUARE_SIZE, selected_piece.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

    pygame.display.update()
    clock.tick(60)
