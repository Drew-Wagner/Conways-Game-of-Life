import pygame, sys, random
from pygame.locals import *

# Number of columns and rows
WIDTH = 100
HEIGHT = 100

# Zoom level
ZOOM = 5

# Initiate pygame and create display surface
pygame.init()
screen = pygame.display.set_mode((WIDTH*ZOOM, HEIGHT*ZOOM))

# Clock to control framerate
fpsClock = pygame.time.Clock()


# Create blank board
board = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

# Randomizes board according to specified density
def randomizeBoard(density=0.15):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            board[i][j] = int(abs(random.gauss(0, 1)) < density)

# Calculates the number of live adjacent cells
def numAdj(x, y):
    s = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if y+1 >= 0 and x+j >=0 and y+1 < HEIGHT and x+j < WIDTH:
                if board[y+i][x+j]:
                    s += 1
    return s

# Draw board and update according to rules
# If a cell is alive and has less than 2 or more than 3 neighbours
# it dies, as if by under or over population.
# If a dead cell has exactly 3 neighbours, it become live, as if
# to simulate reproduction.
def updateAndDrawBoard():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            n = numAdj(j, i)
            if board[i][j] == 1:
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(j*ZOOM, i*ZOOM, ZOOM, ZOOM), 0)
                if n < 2 or n > 3:
                    board[i][j] = 0
            else:
                if n == 3:
                    board[i][j] = 1

# Randomize the board
randomizeBoard()

# Main loop
while True:
    screen.fill((255,255,255)) # Clear the screen
    updateAndDrawBoard() # Draw the board and update

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update display
    pygame.display.update()

    # Limit FPS
    fpsClock.tick(100)
