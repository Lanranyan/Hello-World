"""
 Bounces a rectangle around the screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/-GmKoaX2iMs
"""

import pygame
import os
### to use os: var = os.path.join('filename',

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PEACH = (255, 162, 138)
DRKRED = (153, 0, 0)

pygame.init()

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
BALL_SIZE = 25

pygame.display.set_caption("Bouncing Rectangle + Keys")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

ball = os.path.join('Pictures', 'soccerball.jpg' )
ball1 = pygame.image.load(ball).convert()
ball1 = pygame.transform.rotozoom(ball1, 0, 0.05)


# Starting position of the rectangle
rect_x = 50
rect_y = 50

circle_x = 25
circle_y = 25


# Speed and direction of rectangle
rect_change_x = 0
rect_change_y = 0

circle_change_x = 2
circle_change_y = 2

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_change_x += 5
            if event.key == pygame.K_LEFT:
                rect_change_x -= 5
            if event.key == pygame.K_DOWN:
                rect_change_y += 5
            if event.key == pygame.K_UP:
                rect_change_y -= 5
        elif event.type == pygame.KEYUP:  #makes it so when you left the key, it stops
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                rect_change_x = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                rect_change_y = 0


    # --- Logic
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce the ball if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)
    screen.blit(ball1, (100,100))

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])


    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()