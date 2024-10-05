import pygame
from settings import*




def draw_ranking():
    draw_box_ranking = pygame.draw.rect(display,(branco),(916*mult_posw,238*mult_posh,300*mult_tam,511*mult_tam),border_radius=10)
    font_rank = pygame.font.Font('./assets/roboto/Roboto-Bold.ttf',int(20*mult_tam))
    tela_ranking = font_rank.render(str("Ranking 5 Letras"),True,(corletra))
    display.blit(tela_ranking,(draw_box_ranking.x+115,draw_box_ranking.y+5))

def draw_tutorial():
    display.blit(blur_surf, (0, 0))
    border_box_tutorial = pygame.draw.rect(display,(corcorreta),(479*mult_posw,199*mult_posh,312*mult_tam,412*mult_tam),border_radius=10)
    box_tutorial = pygame.draw.rect(display,(corfundo),(480*mult_posw,200*mult_posh,310*mult_tam,410*mult_tam),border_radius=10)
    tela_tutorial = pygame.font.Font('./assets/roboto/Roboto-Bold.ttf',int(20*mult_tam))
    tutorialbox = pygame.image.load('./assets/tutorialbox.jpg')
    tutorial_image_redmensionada = pygame.transform.scale(tutorialbox,(310*mult_tam,410*mult_tam))
    tutorial_image = tutorial_image_redmensionada.get_rect()
    tutorial_image.topleft = (480 * mult_posw, 200 * mult_posh)
    display.blit(tutorialbox,tutorial_image)
    botao_sair = pygame.draw.rect(display,(48, 48, 48),(box_tutorial.x+115*mult_posw,box_tutorial.y+360*mult_posh,85*mult_tam,40*mult_tam),border_radius=10)
    botao_sair_sair = tela_tutorial.render("Sair",True,branco)
    display.blit(botao_sair_sair,(botao_sair.x+22*mult_posw,botao_sair.y+10*mult_posh))

    return botao_sair
