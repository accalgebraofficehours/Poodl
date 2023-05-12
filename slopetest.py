import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((640, 480))

# Create the player
player = pygame.Rect(100, 100, 50, 50)

# Create the obstacles
obstacles = []
for i in range(10):
    obstacles.append(pygame.Rect(i * 100, 300, 100, 50))

# Set the background color
screen.fill((0, 0, 0))

# Draw the player
pygame.draw.rect(screen, (255, 0, 0), player)

# Draw the obstacles
for obstacle in obstacles:
    pygame.draw.rect(screen, (0, 255, 0), obstacle)

# Update the screen
pygame.display.flip()

# Main loop
while True:
    # Get the events
    events = pygame.event.get()

    # Check for the quit event
    for event in events:
        if event.type == pygame.QUIT:
            break

    # Move the player
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.x -= 10
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.x += 10

    # Check for collisions
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            break

    # If the player collides with an obstacle, the game is over
    if player.colliderect(obstacle):
        break

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
