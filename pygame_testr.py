import pygame
from pygame.locals import*
from pynput import keyboard
import time

pygame.init()


# init some basic color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)

length = 900   
height = 600     
size_screen = (length,height)  # Size

screen = pygame.display.set_caption("Bomberman")
screen = pygame.display.set_mode(size_screen)

background_image = pygame.image.load(r"C:\Users\my pc\Downloads\background.png").convert()
background_image = pygame.transform.scale(background_image, (length, height))

'''load image for player'''

class Player:
    '''Create a player object '''
    def __init__(self):
        self.player_x = 17
        self.player_y = 35
        self.player_width = 50
        self.player_height = 50
        self.velocity = 50
        self.player = (self.player_x,self.player_y)

        self.player_image = pygame.image.load(r"C:\Users\my pc\Downloads\player.png").convert()
        self.player_image = pygame.transform.scale(self.player_image,(55,50))

    def moving(self):
        '''control and process all movement'''
        if event.type == pygame.KEYDOWN:
            print("key down")
            if event.key == pygame.K_UP:
                print("key up")
                if self.player_y > self.player_height:
                    self.player_y -=self.velocity

            elif event.key == pygame.K_DOWN:
                print("key_down")
                if self.player_y + self.player_height <= height:
                    self.player_y +=self.velocity

            elif event.key == pygame.K_LEFT:
                print("key left")
                if self.player_x > self.player_width:
                    self.player_x -= self.velocity

            elif event.key == pygame.K_RIGHT:
                print("key_right") 
                if self.player_x + self.player_width < length:
                    self.player_x += self.velocity


# Main
running = True
while running:
    phuc = Player() # init Player object

    # Take possition of mouse
    # mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(f"x = {mouse_x}, y ={mouse_y}")
    # # time.sleep(1)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            phuc.moving()

        # '''đắp nền trước rồi mới vẽ'''
        # screen.fill(WHITE)a
        # phuc.draw_circle(screen)
        # phuc.moving()
        
        
        screen.blit(background_image, (0, 0))
        player_rect = phuc.player_image.get_rect() # lấy kích thước của ảnh người chơi
        player_rect.center = (phuc.player_x, phuc.player_y) # đặt tâm của ảnh người chơi ở vị trí (player_x, player_y)
        screen.blit(phuc.player_image, phuc.player)

        # screen.blit(background_image,(0,0))

    
    pygame.display.flip()
    fpsClock.tick(FPS)
pygame.quit()