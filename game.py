# Libraries used
import pygame

# Game setup
pygame.init()

# Screen settings
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# More pygame settings
pygame.display.set_caption("Shape Shooter")
clock = pygame.time.Clock()
running = True

class sprite:
    def __init__(self, height, width, position):
        self.height = height
        self.width = width
        self.position = position

# Game loop
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Game rendering

    pygame.display.flip()

    clock.tick(60) # Fps: 60

pygame.QUIT() # Closes game