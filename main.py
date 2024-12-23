import pygame
import sys
import random
from Screen import Screen

pygame.init()

WIDTH, HEIGHT = 400, 400
BLOCK_SIZE = 4
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rows = HEIGHT // BLOCK_SIZE
cols = WIDTH // BLOCK_SIZE
grid = [[0 for _ in range(rows)] for _ in range(cols)]
rectDestaque = None
color = 1

game = Screen(WIDTH, HEIGHT, pygame, "Falling Sand")
SCREEN = game.screen
game.start()

def getYellowColor(value):
    return (255, min(value,255), 0)

def draw_grid(grid):
    """Desenha a grade de 40x40 blocos na tela.
    Args:
        rectDestaque (tuple): Coordenadas do bloco a ser destacado, no formato (linha, coluna).
    """
    for row in range(rows):
        for col in range(cols):
            y, x = row * BLOCK_SIZE, col * BLOCK_SIZE
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            if grid[row][col] != 0:
                pygame.draw.rect(SCREEN, getYellowColor(grid[row][col]), rect)
            else:
                # pygame.draw.rect(SCREEN, WHITE, rect, 1)
                ...


def updateGrid(grid):
    """Atualiza a grade de blocos.
    Args:
        grid (list): Matriz de blocos.
    """
    for row in range(
        rows - 2, -1, -1
    ):  # Começa de baixo para cima, ignorando a última linha.
        for col in range(cols):
            dir = random.choice([-1, 1])
            if col + dir < 0 or col + dir >= cols:
                dir *= -1
            if grid[row][col] != 0 and grid[row + 1][col] == 0:
                grid[row][col] = 0
                grid[row + 1][col] = color
            elif grid[row][col] != 0 and grid[row + 1][col + dir] == 0 :
                grid[row][col] = 0
                grid[row + 1][col + dir] = color


running = True
clock = pygame.time.Clock()
fallTime = 0
while running:
    dt = clock.tick(60)
    fallTime += dt
    game.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            

    SCREEN.fill(BLACK)
    if game.mouse.leftButtomClicked:
        color = 0
    if game.mouse.leftButtomPressed:
        mouseX, mouseY = game.mouse.x, game.mouse.y
        color += 1
        row = mouseY // BLOCK_SIZE
        col = mouseX // BLOCK_SIZE
        if grid[row][col] == 0:
            grid[row][col] = color
    if fallTime > 1:
        fallTime = 0
        updateGrid(grid)

    draw_grid(grid)

    game.late_update()
    pygame.display.flip()


pygame.quit()
sys.exit()
