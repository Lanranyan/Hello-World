
"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""


#import a library of functions called 'pygame'
import pygame
import os   # Operation system
import datetime


def draw_text(text):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text_new = font.render(text, True, RED)
    return text_new

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY_BLUE = (181, 255, 246)
YELLOW = (250, 232, 71)

# Initialize the game engine
pygame.init()

# Set the width and height of the screen [width, height]
os.environ['SDL_VIDEO_HEIGHT_WINDOW_POS'] = '50,50'  #Where it opens
WIDTH = 1200
HEIGHT = 700
size = (WIDTH, HEIGHT)
# size = (700, 500)   #Window Size can skip and input in the code below
screen = pygame.display.set_mode(size)  #Uses the size to create the window
# pygame.display.set_mode command to open up

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SKY_BLUE)

    # --- Drawing code should go here
    #### rect(Surface, color, Rect, width=0) -> Rect
    rect0 = pygame.draw.rect(screen, GREEN, [200, 200, 400, 150], 0)
    #[ starting point x, sp y, width of rect, height o rect], width=0 is line thickness, but 0 fills it

    ### polygon(Surface, color, pointlist, width=0) -> Rect



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
