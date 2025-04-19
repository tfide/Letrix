import pygame
from settings import *



def draw_letras(display,x_cordenada, y_cordenada, input_text):
    font = pygame.font.Font(None, int(130*mult_tam))
    for i, char in enumerate(input_text):
        
        color = corletra
        text_surface = font.render(char, True, color)
        display.blit(text_surface, (x_cordenada, y_cordenada))

        if char.lower() == 'i':
            x_cordenada += text_surface.get_width() + 90*mult_posw  # Espaçamento maior para "i"
            
        else:
            x_cordenada += text_surface.get_width() + 50*mult_posw  # Espaçamento padrão


def drawboxes_branco(): #Desenha os quadrados brancos
        for j in range(6):
            for i in range(5):                                                                                     
                pygame.draw.rect(display, branco, (100*mult_posw + i * 110*mult_posw, 20*mult_posh + j * 120*mult_posh, 100*mult_tam, 100*mult_tam), border_radius=10)

def draw_tempovitoria(font_timer,tempo_vitoria):         #Timer que fica rodando equanto o jogador joga
        box_timer = pygame.draw.rect(display,(corfundo), (700*mult_posw,300*mult_posh,249*mult_tam,120*mult_tam), border_radius=10)
        box_font_timer = font_timer.render(str(tempo_vitoria), True,branco)
        display.blit(box_font_timer,(box_timer.x+10*mult_posw,box_timer.y+25*mult_posh))

def box_borda():
    corbox = pygame.image.load('./assets/cor.png')
    corbox = pygame.transform.scale(corbox, (50, 50))
    display.blit(corbox,(700*mult_posw,350*mult_posh))

def draw_telavitoria(tempo_vitoria,tentativas,palavra_sorteada,font_roboto,font_roboto2,estrela_branca,estrela_azul): #Após acertar a palavra sorteada, exibira a tela de vitória
    display.blit(blur_surf, (0, 0))
    tela_vitoria = pygame.draw.rect(display,(40,40,40),(430*mult_posw,92*mult_posh,471*mult_tam,557*mult_tam))
    tela_vitoria_font = font_roboto2.render(str("Vitória"),True,(corcorreta))
    tela_vitoria_font2 = font_roboto.render(str(str(tempo_vitoria)+" seg"),True,(branco))
    tela_vitoria_font3 = font_roboto.render(str(str(tentativas)+" tentativas"),True,(branco))
    tela_vitoria_font4 = font_roboto.render(str(str(palavra_sorteada.upper())),True,(branco))
    
    display.blit(tela_vitoria_font,(tela_vitoria.x+155*mult_posw,tela_vitoria.y+80*mult_posh)) #Desenha o escrito "Vitoria"
    display.blit(tela_vitoria_font2,(tela_vitoria.x+30*mult_posw,tela_vitoria.y+253*mult_posh)) #Desenha o tempo gasto em segundos
    display.blit(tela_vitoria_font3,(tela_vitoria.x+250*mult_posw,tela_vitoria.y+253*mult_posh)) #Desenha o numero de tentativas
    display.blit(tela_vitoria_font4,(tela_vitoria.x+155*mult_posw,tela_vitoria.y+360*mult_posh)) #Desenha a palavras sorteada

    i = 0
    while i < 5:
        display.blit(estrela_branca,(tela_vitoria.x+130*mult_posw+60*i,tela_vitoria.y+22)) #Desenha as estelas brancas que estão na pasta assets
        i +=1
    i = 0
    tentativa_estrela = 6 - tentativas                                         #Quantas estrelas azuis vai desenhar
    while i < tentativa_estrela:
        display.blit(estrela_azul,(tela_vitoria.x+130*mult_posw+60*i,tela_vitoria.y+22)) #Desenha por cima das brancas azuis de acordo com o numero de tentativas
        i+=1

def draw_teladerrota(tentativas,palavra_sorteada,font_roboto,font_roboto2,estrela_branca):
    display.blit(blur_surf, (0, 0))
    tela_derrota = pygame.draw.rect(display,(40,40,40),(430*mult_posw,92*mult_posh,471*mult_tam,557*mult_tam))
    tela_derrota_font = font_roboto2.render(str("Derrota"),True,(255, 91, 79))
    tela_derrota_font3 = font_roboto.render(str(str(tentativas)+" tentativas"),True,(branco))
    tela_derrota_font4 = font_roboto.render(str(str(palavra_sorteada.upper())),True,(branco))
    
    display.blit(tela_derrota_font,(tela_derrota.x+155*mult_posw,tela_derrota.y+80*mult_posh)) #Desenha o escrito "Derrota"
    display.blit(tela_derrota_font3,(tela_derrota.x+125*mult_posw,tela_derrota.y+253*mult_posh)) #Desenha o numero de tentativas
    display.blit(tela_derrota_font4,(tela_derrota.x+155*mult_posw,tela_derrota.y+360*mult_posh)) #Desenha a palavras sorteada

    i = 0
    while i < 5:
        display.blit(estrela_branca,(tela_derrota.x+130*mult_posw+60*i,tela_derrota.y+22)) #Desenha as estelas brancas que estão na pasta assets
        i +=1
    
    tela_vitoria_fontexit = font_roboto.render(str("Menu"),True,(corletra))
    botao_menu = pygame.draw.rect(display,(255, 91, 79),(546*mult_posw,538*mult_posh,240*mult_tam,78*mult_tam),border_radius=10)
    display.blit(tela_vitoria_fontexit,(botao_menu.x+70*mult_posw,botao_menu.y+10*mult_posh))

def mostrar_popup():
    
    font = pygame.font.Font(None, 45)
    texto_popup = font.render('Esta Palavra não existe !!', True, (branco))
    display.blit(texto_popup,(1000,250))

