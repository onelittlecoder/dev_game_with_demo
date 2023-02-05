import pygame
import random

# Initialize game
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set screen size and title
screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("2048")

# Define game grid
grid = [[0 for x in range(4)] for y in range(4)]

# Populate two random cells with 2s or 4s
for i in range(2):
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    grid[x][y] = 2 if random.randint(0, 1) else 4

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update grid based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass
    elif keys[pygame.K_DOWN]:
        pass
    elif keys[pygame.K_LEFT]:
        pass
    elif keys[pygame.K_RIGHT]:
        pass

    # Draw grid
    screen.fill(white)
    for row in range(4):
        for col in range(4):
            pygame.draw.rect(screen, black, (row*100, col*100, 100, 100), 1)
            if grid[row][col]:
                font = pygame.font.Font(None, 36)
                text = font.render(str(grid[row][col]), True, black)
                screen.blit(text, (row*100 + 50, col*100 + 50))

    # Update screen
    pygame.display.update()

# Quit game
pygame.quit()
