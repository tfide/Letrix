import pygame
from settings import *


def drawboxes_branco(): #Desenha os quadrados brancos
        for j in range(6):
            for i in range(4):                                                                                     
                pygame.draw.rect(display, branco, (100*mult_posw + i * 110*mult_posw, 20*mult_posh + j * 120*mult_posh, 100*mult_tam, 100*mult_tam), border_radius=10)

def drawbox_letra(display,y_offset,colors):
    
    for i in range(4):
        pygame.draw.rect(display, colors[i], (100*mult_posw + i * 110*mult_posw, -100*mult_posh + y_offset*mult_posh, 100*mult_tam, 100*mult_tam), border_radius=10)