import pygame
import random

import time

from settings import*
from game_4_letras import game_4letras
from drawbox_letra import drawbox_letra
from draw import draw_letras, drawboxes_branco,box_borda, draw_tempovitoria, draw_telavitoria,draw_teladerrota, mostrar_popup
from draw_menu import draw_ranking, draw_tutorial
from timerr import*




# ____________________________________________________________________________________________________
ranking = []
ranking4 =[]

def game5_letras(player_name):
    
    pygame.init()
    pygame.display.set_caption("Letrix")


    font_roboto = pygame.font.Font('./assets/roboto/Roboto-Bold.ttf',int(40*mult_tam))
    font_roboto2 = pygame.font.Font('./assets/roboto/Roboto-Bold.ttf',int(50*mult_tam))
    font2 = pygame.font.SysFont(None, int(55*mult_tam)) #Font do botão reset
    font_timer = pygame.font.SysFont(None,int(150*mult_tam))
    estrela_branca= pygame.image.load('./assets/estrelabranca.png')
    estrela_azul= pygame.image.load('./assets/estrelaazul.png')
    tutorialbox = pygame.image.load('./assets/tutorialbox.jpg')

    mouse_pos = (0,0)
    
    box_bordas = False
    draw_vitoria = False
    draw_derrota = False
    pop_up = False
    dica = False
    


    # Código que sorteia a palavra e transforma a palavra em um array de letras
    
    nome_tema_sorteado = random.choice(list(temas.keys()))
    tema_sorteado = temas[nome_tema_sorteado]
    palavra_sorteada = random.choice(tema_sorteado)
    palavra_lista = []
    for letra in palavra_sorteada:
        palavra_lista.append(letra)
    print(palavra_lista)
    print(nome_tema_sorteado)
    
    
    def draw():
        
        for i, y_offset in enumerate(y_offsets):
            draw_letras(display,110*mult_posw, 30*mult_posh + y_offset*mult_posh, input_texts[i])

    gameLoop = True
    if __name__ == "__main__":
        y_offsets = [0]
        colors = [[branco] * 5]  # Inicializa a lista de cores com branco
        input_texts = ['']  # Lista para armazenar os textos de entrada
        tentativas = 0  # Contador de tentativas


        while gameLoop:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    gameLoop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input_texts[-1] = input_texts[-1][0:-1]
                    elif event.key == pygame.K_SPACE:
                        pass
                    elif len(input_texts[-1]) < 5 and event.unicode.isalpha() :
                        input_texts[-1] += event.unicode.upper()
                    
                    elif event.key == pygame.K_RETURN and len(input_texts[-1]) == 5 and tentativas < 6:  # Verifica se Enter foi pressionado e se o número de tentativas é menor que 5
                        
                        if input_texts[-1].lower() not in palavras_ptbr:
                            print("Essa palavra não existe neste jogo")
                            pop_up = True
                            tempo_exibicao = time.time()

                        if input_texts[-1].lower() in palavras_ptbr:
                            tentativas += 1  # Incrementa o contador de tentativas
                            new_colors = []
                            
                            if input_texts[-1].lower() == palavra_sorteada:
                                print("Palavra correta!")
                                new_colors = [corcorreta] * 5  # Se a palavra estiver correta, todas as caixas ficam verdes
                                tempo_vitoria = int(get_time()) # Recebe o tempo que passou até dar vitoria
                                draw_vitoria = True    #Ativa a função de desenhar o tempo parado na tela (desenhando por cima do timer em tempo real)
                                
                                
                            else:
                                for i, letra in enumerate(input_texts[-1].lower()):
                                    if letra == palavra_lista[i]:
                                        new_colors.append(corcorreta)  # Letra correta
                                    elif letra in palavra_lista:
                                        new_colors.append(corneutra)  # Letra existe na palavra mas está na posição errada
                                    else:
                                        new_colors.append(corerrada)  # Letra incorreta
                                print("Palavra incorreta!")
                                
                            

                            colors.append(new_colors)  # Adiciona as novas cores à lista de cores
                            input_texts.append('')  # Adiciona uma nova linha de texto
                            y_offsets.append(y_offsets[-1] + 120)  # Adiciona um novo deslocamento vertical


                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if quit_button.collidepoint(mouse_pos):
                        return game5_letras
            display.fill([35, 35, 35])


            drawboxes_branco()      # Desenha os vários quadrados brancos

            
            for i, y_offset in enumerate(y_offsets):
                drawbox_letra(display,y_offset, colors[i])  # Desenha todas as linhas de caixas com as cores apropriadas

            draw()



            quit_button = pygame.draw.rect(display, (255, 100, 0 ), (650*mult_posw, 20*mult_posh, 166*mult_tam, 50*mult_tam))
            quit_text = font2.render("Voltar", True, corletra )
            display.blit(quit_text, (quit_button.x + 30, quit_button.y + 10))

            # Tutorial
            tutorial_image_redmensionada = pygame.transform.scale(tutorialbox,(310*mult_tam,410*mult_tam))
            tutorial_image = tutorial_image_redmensionada.get_rect()
            tutorial_image.topleft = (1000 * mult_posw, 200 * mult_posh)
            display.blit(tutorialbox,tutorial_image)

            if input_texts[-1].lower() == "maria":
                box_bordas = True
            if box_bordas:
                box_borda()

            # Desenha o timer na tela em tempo real
            tempo_correndo = int(get_time())
            box_font_timer = font_timer.render(str(tempo_correndo), True,branco)
            display.blit(box_font_timer,(800*mult_posw,300*mult_posh))

        
            if pop_up:
                if time.time() - tempo_exibicao < 2:
                    pop_up_text = mostrar_popup()
                    #display.blit(pop_up_text, (100, 100))  # Exibe o pop-up na tela
                else:
                    pop_up = False  # Oculta o pop-up após 2 segundos

            if tentativas > 2:
                dica = True
            if dica:
                box_dica = pygame.draw.rect(display,(48, 48, 48),(1100*mult_posw,550*mult_posh,110*mult_tam,60*mult_tam),border_radius=10)
                box_dica_font = font_roboto.render("Dica !",True,branco)
                display.blit(box_dica_font,(box_dica.x+5*mult_posw,box_dica.y+10*mult_posh))
                
                if box_dica.collidepoint(mouse_pos):
                    box_dica_font = font_roboto.render((nome_tema_sorteado),True,branco)
                    display.blit(box_dica_font,(box_dica.x-10*mult_posw,box_dica.y+60*mult_posh))
                

            if draw_derrota:
                draw_teladerrota(tentativas,palavra_sorteada,font_roboto,font_roboto2,estrela_branca)
            
            # Desenha o tempo de segundos que demorou
            if draw_vitoria:
                draw_tempovitoria(font_timer,tempo_vitoria)
                draw_telavitoria(tempo_vitoria,tentativas,palavra_sorteada,font_roboto,font_roboto2,estrela_branca,estrela_azul)
                
                #Desenha botão Menu
                tela_vitoria_fontexit = font_roboto.render(str("Menu"),True,(corletra))
                botao_menu = pygame.draw.rect(display,(125,241,245),(546*mult_posw,538*mult_posh,240*mult_tam,78*mult_tam),border_radius=10)
                display.blit(tela_vitoria_fontexit,(botao_menu.x+70,botao_menu.y+10))
            

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if botao_menu.collidepoint(mouse_pos):
                        ranking.append((player_name, tempo_vitoria))
                        return tempo_vitoria
            if tentativas == 6:
                    draw_derrota = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return


            pygame.display.update()
            
    pygame.quit()






#_______________________________________________________________________________________________________________________________________________________________

def menu():

    player_name = ""
    cor_button5letras = (corerrada)
    cor_button4letras = (corerrada)
    pygame.init()
    pygame.display.set_caption("Letrix")

    # Load e Play das Musicas
    pygame.mixer.init()
    current_song = 0
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()
    
    font_menu = pygame.font.SysFont(None,int(71*mult_tam))
    font_rank = pygame.font.Font('./assets/roboto/Roboto-Bold.ttf',int(20*mult_tam))
    font_credito = pygame.font.Font('./assets/roboto/Roboto-Bold.ttf',int(10*mult_tam))
    logo_letrix = pygame.image.load('./assets/letrixpng24.png')
    drawtutorial = False
    botao_sair_tutorial = draw_tutorial()
    cor_musica = (48,48,48)
    paused = False

    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                else:
                    if len(player_name) <21:
                        player_name += event.unicode
                if event.key == pygame.K_RETURN:
                    player_name = player_name[:-1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button5letras.collidepoint(event.pos) and player_name and drawtutorial == False:
                    start_timer()
                    tempo_final = game5_letras(player_name)
                    print(tempo_final)
                    player_name = ""
                if button4letras.collidepoint(event.pos) and player_name and drawtutorial == False:
                    start_timer()
                    game_4letras()
                    player_name = ""
                if box_tutorial.collidepoint(event.pos):
                    drawtutorial = True
                if botao_sair_tutorial.collidepoint(event.pos):
                    drawtutorial = False
                if botao_sair.collidepoint(event.pos) and drawtutorial == False:
                    return
            
            
            # Verifica se a caixa de música foi clicada
                if box_musica.collidepoint(event.pos):
                    if paused:
                        pygame.mixer.music.unpause()
                        paused = False
                        cor_musica = (48,48,48)
                    else:
                        pygame.mixer.music.pause()
                        paused = True
                        cor_musica = (138, 37, 37)


            # Loop para tocar a próxima música caso acabe e volta para a primeira caso acabe
            if not pygame.mixer.music.get_busy() and not paused:
                current_song += 1
                if current_song >= len(playlist):
                    current_song = 0  # Volta para a primeira música
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
            
# __________________________________________________________________________________________________________________________________________________________                    

        display.fill([35,35,35])
        font = pygame.font.Font(None, int(36*mult_tam))
        text = font.render("Digite seu nome: " + player_name, True, (255, 255, 255))
        display.blit(text, (200*mult_posw, 300*mult_posh))
        

        #Botão 5 letras
        if player_name:
            cor_button5letras = (25, 245, 252)
            cor_button4letras = (25, 173, 252)
        else:
            cor_button5letras = (corerrada)
            cor_button4letras = (corerrada)
        button5letras = pygame.draw.rect(display,(cor_button5letras), (507*mult_posw,539*mult_posh,249*mult_tam,93*mult_tam), border_radius=10)
        button5letras_font = font_menu.render("5 LETRAS", True,corletra)
        display.blit(button5letras_font,(button5letras.x+10,button5letras.y+25))

        # Botão 4 letras
        button4letras = pygame.draw.rect(display,(cor_button4letras), (507*mult_posw,409*mult_posh,249*mult_tam,93*mult_tam), border_radius=10)
        button4letras_font = font_menu.render("4 LETRAS", True,corletra)
        display.blit(button4letras_font,(button4letras.x+10,button4letras.y+25))


        # Exibir o ranking
        draw_ranking()
        y_offset = 0
        for i, (name, (tempo)) in enumerate(sorted(ranking, key=lambda x: x[1])):
            rank_text = font_rank.render(f"{name} ", True, (corletra))
            rank_text2 = font_rank.render(f"{tempo:.0f}s", True, (corletra))
            display.blit(rank_text, (920*mult_tam,275*mult_tam+ y_offset))
            display.blit(rank_text2, (1150*mult_tam,275*mult_tam+ y_offset))
            y_offset += 35


        #Logo do Jogo
        logo_redmensionada = pygame.transform.scale(logo_letrix,(500*mult_tam,176*mult_tam))
        logoxy = logo_redmensionada.get_rect()
        logoxy.center = (640*mult_posw,100*mult_posh)
        display.blit(logo_redmensionada,logoxy)

        #Botão Sair
        botao_sair = pygame.draw.rect(display,(96, 38, 255),(515*mult_posw,670*mult_posh,230*mult_tam,70*mult_tam),border_radius=10)
        botao_sair_font = font_menu.render("Sair",True,corletra)
        display.blit(botao_sair_font,(botao_sair.x+65*mult_posw,botao_sair.y+10*mult_posh))

        #Botão do Tutorial
        box_tutorial = pygame.draw.rect(display,(48, 48, 48),(5*mult_posw,400*mult_posh,85*mult_tam,40*mult_tam),border_radius=10)
        box_tutorial_font = font_rank.render("Tutorial",True,branco)
        display.blit(box_tutorial_font,(box_tutorial.x+5*mult_posw,box_tutorial.y+10*mult_posh))


        # Créditos
        box_creditos = pygame.draw.rect(display,(corfundo),(5*mult_posw,487*mult_posh,85*mult_tam,40*mult_tam),border_radius=10)
        box_creditos_font = font_credito.render("Créditos a @fewtile (Músicas)",True,branco)
        display.blit(box_creditos_font,(box_creditos.x+5*mult_posw,box_creditos.y+10*mult_posh))

        #Botão Musica
        box_musica = pygame.draw.rect(display,(cor_musica),(5*mult_posw,450*mult_posh,85*mult_tam,40*mult_tam),border_radius=10)
        box_musica_font = font_rank.render("Musica",True,branco)
        display.blit(box_musica_font,(box_musica.x+5*mult_posw,box_musica.y+10*mult_posh))




        if event.type == pygame.MOUSEMOTION:                                         #Se mouse passa por cima da imagem, ela ganhar uma cor diferente
            if botao_sair.collidepoint(event.pos):
                pygame.draw.rect(display,(119, 74, 240),(515*mult_posw,670*mult_posh,230*mult_tam,70*mult_tam),border_radius=10)
                display.blit(botao_sair_font,(botao_sair.x+65*mult_posw,botao_sair.y+10*mult_posh))
            if button4letras.collidepoint(event.pos) and player_name:
                button4letras = pygame.draw.rect(display,(92, 198, 255), (507*mult_posw,409*mult_posh,249*mult_tam,93*mult_tam), border_radius=10)
                display.blit(button4letras_font,(button4letras.x+10,button4letras.y+25))
            if button5letras.collidepoint(event.pos) and player_name:
                button5letras = pygame.draw.rect(display,(115, 246, 250), (507*mult_posw,539*mult_posh,249*mult_tam,93*mult_tam), border_radius=10)
                display.blit(button5letras_font,(button5letras.x+10,button5letras.y+25))
            if box_tutorial.collidepoint(event.pos):
                box_tutorial = pygame.draw.rect(display,(69, 69, 69),(5*mult_posw,400*mult_posh,85*mult_tam,40*mult_tam),border_radius=10)
                display.blit(box_tutorial_font,(box_tutorial.x+5*mult_posw,box_tutorial.y+10*mult_posh))
            if box_musica.collidepoint(event.pos):
                box_musica = pygame.draw.rect(display,(69, 69, 69),(5*mult_posw,450*mult_posh,85*mult_tam,40*mult_tam),border_radius=10)
                display.blit(box_musica_font,(box_musica.x+5*mult_posw,box_musica.y+10*mult_posh))
        
        if drawtutorial:
            draw_tutorial()

        pygame.display.update()
        
        


if __name__ == "__main__":
    menu()