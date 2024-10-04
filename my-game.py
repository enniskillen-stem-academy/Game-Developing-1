import pygame

# Initialize pygame
pygame.init()

# Constants for the game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Complete Game")

# Define colors
PLAYER_COLOR = (255, 165, 0)  # Orange
OBSTACLE_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Player attributes
player_x, player_y = 300, 200
player_size = 40

# Obstacle attributes
obstacle_x, obstacle_y = 100, 150
obstacle_size = 50

# Game loop variable
running = True

# Game loop
while running:
    # Check for events (such as quitting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the player (rectangle)
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_size, player_size))

    # Draw the obstacle (rectangle)
    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))

    # Movement for the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 1
    if keys[pygame.K_RIGHT]:
        player_x += 1
    if keys[pygame.K_UP]:
        player_y -= 1
    if keys[pygame.K_DOWN]:
        player_y += 1

    # Move the obstacle down
    obstacle_y += 2
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_y = 0  # Reset obstacle position when it goes off-screen

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_size, obstacle_size)

    if player_rect.colliderect(obstacle_rect):
        print("Collision Detected!")

    # Update the screen
    pygame.display.update()

# Quit pygame when the loop is finished
pygame.quit()
