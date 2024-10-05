import pygame
from settings import *

def drawbox_letra(display,y_offset,colors):
    
    for i in range(5):
        pygame.draw.rect(display, colors[i], (100*mult_posw + i * 110*mult_posw, -100*mult_posh + y_offset*mult_posh, 100*mult_tam, 100*mult_tam), border_radius=10)


