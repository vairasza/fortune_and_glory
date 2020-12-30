import pygame
from pygame.locals import *
import data.Constants as Constants
import os

#/Users/micha/Downloads
def load_img(name):
    img_name = os.path.join('data', name)
    img = pygame.image.load(img_name)
    img = pygame.transform.scale(img, (60, 60))
    return img

def move_linux(x, y):
    screen.blit(load_img('download.png'), (x, y))

def draw_rect(x,y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rect_x_l = 200
    rect_x_r = 300
    rect_y_t = 200
    rect_y_b = 300

    if mouse_x >= rect_x_l and mouse_x <= rect_x_r and mouse_y >= rect_y_t and mouse_y <= rect_y_b:
        surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        surface.set_alpha(40)
        surface.fill(blue)
        screen.blit(surface, (rect_x_l,rect_y_t))
    else:
        rect = pygame.Rect(rect_x_l, rect_y_t, 100, 100)
        pygame.draw.rect(screen, blue, rect)

def draw_blocks(x,y,name):
    img_name = os.path.join('Isometric_Tiles_Pixel_Art/Blocks', name)
    img = pygame.image.load(img_name)
    screen.blit(img, (x,y))
    

pygame.init()
screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption(Constants.GAME_NAME)

clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

font = pygame.font.Font(None, 36)
text = font.render("Hello There", 1, (10, 10, 10)) #=> calc surrounding rect
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

#objects

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

x = 0
y = 0
x_f = 0
y_f = 0
quit = False
black = (0,0,0)
blue = (0,0,255)

# Event loop
while not quit:

    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True
        
        keys = pygame.key.get_pressed()
        #keyevents
        if keys[K_w]:
            y_f = -1
        elif keys[K_s]:
            y_f = 1
        else:
            y_f = 0

        if keys[K_a]:
            x_f = -1
        elif keys[K_d]:
            x_f = 1
        else:
            x_f = 0

    screen.blit(background, (0, 0))
    draw_rect(x,y)

    row = 49
    x_start = screen.get_width() + 50
    y_start = -50
    x_step = 33
    y_step = 17
    x_move = x_step * 2

    for j in range(row):
        blocks = j * 2
        for i in range (blocks):
            draw_blocks(x_start + i * x_step - j * x_move, y_start + i * y_step, 'blocks_1.png')

    x += x_f
    y += y_f
    move_linux(x, y)

    pygame.display.update()
    clock.tick(60)