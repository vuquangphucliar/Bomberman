import pygame
from pygame.locals import *
import os

pygame.init()

# Constants
WIDTH = 900
HEIGHT = 600
PLAYER_SPEED = 51
# Basic color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

# Load images
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (50, 50))
bomb_image = pygame.image.load("bomb.png")
bomb_image = pygame.transform.scale(bomb_image, (50, 50))

# Initialize font
font_small = pygame.font.SysFont('sans', 10)

# Define Player class
class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move_up(self):
        if self.y > 65 and (self.x - 17) / 51 % 2 == 0:
            self.y -= PLAYER_SPEED

    def move_down(self):
        if self.y < 500 and (self.x - 17) / 51 % 2 == 0:
            self.y += PLAYER_SPEED

    def move_left(self):
        if self.x > 45 and (self.y - 35) / 51 % 2 == 0:
            self.x -= PLAYER_SPEED

    def move_right(self) :
        if self.x < 800 and (self.y - 35) / 51 % 2 == 0:
            self.x += PLAYER_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Bomb:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.explode_time = pygame.time.get_ticks() + 5000  # set 5 seconds timer

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# Initialize player object
player = Player(17, 35, player_image)

# Initialize bomb object
bomb = None

# Initialize screen
pygame.display.set_caption("Bomberman")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()
            elif event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_SPACE and not bomb:  # create bomb when space key is pressed
                bomb = Bomb(player.x, player.y, bomb_image)


    # Draw images and text
            
    screen.blit(background_image, (0, 0))
    if bomb:
        bomb.draw(screen)
        if pygame.time.get_ticks() > bomb.explode_time:  # explode bomb after 5 seconds
            bomb = None
    player.draw(screen)


    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_mouse = font_small.render("(" + str(mouse_x) + "," + str(mouse_y) + ")", True, BLACK)
    screen.blit(text_mouse, (mouse_x + 10, mouse_y))

    # Update screen
    pygame.display.flip()

# Quit game
pygame.quit()