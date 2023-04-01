import pygame
from pygame.locals import*
from pynput import keyboard
import time

pygame.init()

font_small = pygame.font.SysFont('sans', 10)

width = 600
length = 900

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

player_x = 833
player_y = 35
# player_x = 830
# player_y = 36
player_width = 50
player_height = 50
player = [player_x, player_y] # tọa độ người chơi


screen = pygame.display.set_caption("Bomberman")
screen = pygame.display.set_mode((length, width))


background_image = pygame.image.load(r"C:\Users\my pc\Downloads\background.png").convert()
background_image = pygame.transform.scale(background_image, (length, width))

player_image = pygame.image.load(r"C:\Users\my pc\Downloads\player.png").convert()
player_image = pygame.transform.scale(player_image, (50, 50))

player_speed = 51

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP):
                if player[1] > 65:
                    player[1] -= player_speed
                    print("up")

            elif (event.key == pygame.K_DOWN):
                    if player[1] < 500:
                        player[1] = player[1] + player_speed
                        print("down")

            elif (event.key == pygame.K_LEFT):
                if player[0] > 45:
                    player[0] = player[0] - player_speed
                    print("left")

            elif (event.key == pygame.K_RIGHT):
                if player[0] < 800:
                    player[0] = player[0] + player_speed
                    print("right")


    screen.blit(background_image, (0, 0))
    player_rect = player_image.get_rect() # lấy kích thước của ảnh người chơi
    player_rect.center = (player_x, player_y) # đặt tâm của ảnh người chơi ở vị trí (player_x, player_y)
    screen.blit(player_image, player)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    text_mouse = font_small.render("(" + str(mouse_x) + "," + str(mouse_y) + ")", True, BLACK)
    screen.blit(text_mouse, (mouse_x + 10, mouse_y))

    pygame.display.flip()

pygame.quit()