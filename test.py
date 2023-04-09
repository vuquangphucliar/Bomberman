import time
import pygame
from pygame.locals import *
import os

pygame.init()

# Constants
WIDTH = 900
HEIGHT = 600
PLAYER_SPEED = 51
player_start_x = 17
player_start_y = 35

# game space
LEFT = 45
RIGHT = 800
UP = 60
DOWN = 500

# Basic color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

# Load images
background_image = pygame.image.load(r"C:\Users\nguye\Documents\Bomberman\picture\background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
player_image = pygame.image.load(r"C:\Users\nguye\Documents\Bomberman\picture\player.png")
player_image = pygame.transform.scale(player_image, (45, 50))
bomb_image = pygame.image.load(r"C:\Users\nguye\Documents\Bomberman\picture\bomb.png")
bomb_image = pygame.transform.scale(bomb_image, (45, 45))
wall_image = pygame.image.load(r"C:\Users\nguye\Documents\Bomberman\picture\wall.png")
wall_image = pygame.transform.scale(wall_image, (50, 50))
explosion_image = pygame.image.load(r"C:\Users\nguye\Documents\Bomberman\picture\explosion.png")
explosion_image = pygame.transform.scale(explosion_image, (51, 51))

# Initialize font
font_small = pygame.font.SysFont('sans', 10)

#wall list
wall_list = [(17, 188), (17, 392),
            (68, 239), (68, 443), 
            (118, 86), (118, 188), (118, 290), (118, 392), (118, 493), 
            (168, 35), (168, 137), (168, 341), (168, 543), 
            (219, 86), (219, 290), (219, 493), 
            (269, 137), (269, 239), (269, 341), 
            (321, 188), (321, 290), (321, 392), (321, 493), 
            (371, 137), (371, 341), (371, 443), (371, 543), 
            (423, 86), (423, 188), (423, 392), 
            (474, 35), (474, 239), (474, 341), 
            (524, 188), (524, 493), 
            (576, 35), (576, 341), (576, 443), (576, 543), 
            (628, 86), (628, 188), (628, 290), (628, 392), 
            (680, 137), (680, 239), (680, 443), 
            (732, 86), (732, 188), (732, 392), (732, 493), 
            (783, 35), (783, 137), (783, 239), (783, 341), (783, 543), 
            (834, 188), (834, 392)]

# list of cells that cannot be entered
blocked_coordinates = [(17, 188), (17, 392), 
                       (68, 239), (68, 443), 
                       (119, 86), (119, 188), (119, 290), (119, 392), (119, 494), 
                       (170, 35), (170, 137), (170, 341), (170, 545), 
                       (221, 86), (221, 290), (221, 494), 
                       (272, 137), (272, 239), (272, 341), 
                       (323, 188), (323, 290), (323, 392), (323, 494), 
                       (374, 137), (374, 341), (374, 443), (374, 545), 
                       (425, 86), (425, 188), (425, 392), 
                       (476, 35), (476, 239), (476, 341), 
                       (527, 188), (527, 494), 
                       (578, 35), (578, 341), (578, 443), (578, 545), 
                       (629, 86), (629, 188), (629, 290), (629, 392), 
                       (680, 137), (680, 239), (680, 443), 
                       (731, 86), (731, 188), (731, 392), (731, 494), 
                       (782, 35), (782, 137), (782, 239), (782, 341), (782, 545), 
                       (833, 188), (833, 392)]

# Define Player class
class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move_up(self):
        if (self.x, self.y - PLAYER_SPEED) not in blocked_coordinates and self.y > UP and (self.x - 17) / PLAYER_SPEED % 2 == 0:
            self.y -= PLAYER_SPEED

    def move_down(self):
        if (self.x, self.y + PLAYER_SPEED) not in blocked_coordinates and self.y < DOWN and (self.x - 17) / PLAYER_SPEED % 2 == 0:
            self.y += PLAYER_SPEED

    def move_left(self):
        if (self.x - PLAYER_SPEED, self.y) not in blocked_coordinates and self.x > LEFT and (self.y - 35) / PLAYER_SPEED % 2 == 0:
            self.x -= PLAYER_SPEED

    def move_right(self):
        if (self.x + PLAYER_SPEED, self.y) not in blocked_coordinates and self.x < RIGHT and (self.y - 35) / PLAYER_SPEED % 2 == 0:
            self.x += PLAYER_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# define bomb class
class Bomb:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.explode_time = pygame.time.get_ticks() + 4000  # set 5 seconds timer
        self.exploded = False

    def draw(self, screen):
        if not self.exploded:
            screen.blit(self.image, (self.x, self.y))
            if pygame.time.get_ticks() > self.explode_time:  # explode bomb after 5 seconds
                self.image = explosion_image
                self.explode_time = pygame.time.get_ticks() + 800  # set 1 second timer for flame
                self.exploded = True
        else:
            if pygame.time.get_ticks() > self.explode_time:  # remove flame after 1 second
                self.image = None

        if self.image:
            screen.blit(self.image, (self.x, self.y))
        
# define wall class
class Wall:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# Initialize player object
player = Player(player_start_x, player_start_y, player_image)

# Initialize bomb object
bomb = None

# Initialize the explosion object
explosion = None

# Initialize wall objects
wall_objects = []
for wall_pos in wall_list:
    wall = Wall(wall_pos[0], wall_pos[1], wall_image)
    wall_objects.append(wall)

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
        if pygame.time.get_ticks() > bomb.explode_time:  # explode bomb after 3 seconds
            bomb = None
        
    player.draw(screen)
    
    # Draw wall objects
    for wall in wall_objects:
        wall.draw(screen)

    # print the cursor coordinates to the screen
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_mouse = font_small.render("(" + str(mouse_x) + "," + str(mouse_y) + ")", True, BLACK)
    screen.blit(text_mouse, (mouse_x + 10, mouse_y))

    # Update screen
    pygame.display.flip()

# Quit game
pygame.quit()