import random
import pygame

from draw import gambiarra1, draw_tempovitoria, draw_telavitoria,draw_teladerrota,draw_letras
from settings import*
from timerr import*



from draw_4letras import drawbox_letra, drawboxes_branco
def game_4letras():
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
    
    draw_vitoria = False
    draw_derrota = False


    # Código que sorteia a palavra e transforma a palavra em um array de letras
    
    nome_tema_sorteado = random.choice(list(temas4.keys()))
    tema_sorteado = temas4[nome_tema_sorteado]
    palavra_sorteada = random.choice(tema_sorteado)
    print(palavra_sorteada.split())
    palavra_lista = []
    for letra in palavra_sorteada:
        palavra_lista.append(letra)
    print(palavra_lista)
    print(nome_tema_sorteado)
    
    
    def draw():
        
        for i, y_offset in enumerate(y_offsets):
            draw_letras(display,110*mult_posw, 30*mult_posh + y_offset*mult_posh, input_texts[i])

    gameLoop = True
    if gameLoop:
        y_offsets = [0]
        colors = [[branco] * 4]  # Inicializa a lista de cores com branco
        input_texts = ['']  # Lista para armazenar os textos de entrada
        tentativas = 0  # Contador de tentativas

        while gameLoop:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    gameLoop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input_texts[-1] = input_texts[-1][0:-1]
                    elif len(input_texts[-1]) < 4 and event.unicode.isalpha():
                        input_texts[-1] += event.unicode.upper()
                    elif event.key == pygame.K_RETURN and len(input_texts[-1]) == 4 and tentativas < 6:  # Verifica se Enter foi pressionado e se o número de tentativas é menor que 5
                        tentativas += 1  # Incrementa o contador de tentativas
                        new_colors = []
                        
                        if input_texts[-1].lower() == palavra_sorteada:
                            print("Palavra correta!")
                            new_colors = [corcorreta] * 4  # Se a palavra estiver correta, todas as caixas ficam verdes
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
                    if quit_button4.collidepoint(mouse_pos):
                        return
                
                
                        
            display.fill([35,35,35])

            
            drawboxes_branco()      # Desenha os vários quadrados brancos

            
            for i, y_offset in enumerate(y_offsets):
                drawbox_letra(display,y_offset, colors[i])  # Desenha todas as linhas de caixas com as cores apropriadas

            draw()
            
            #gambiarra1()              # Gabiarra para tampar a primeira filera de Quadrados

            # Desenha o botão de reset
            quit_button4 = pygame.draw.rect(display, (255, 100, 0), (650*mult_posw, 20*mult_posh, 166*mult_tam, 50*mult_tam))
            quit_text4 = font2.render("voltar", True,corletra)
            display.blit(quit_text4, (quit_button4.x + 30, quit_button4.y + 10))


            # Tutorial
            tutorial_image_redmensionada = pygame.transform.scale(tutorialbox,(310*mult_tam,410*mult_tam))
            tutorial_image = tutorial_image_redmensionada.get_rect()
            tutorial_image.topleft = (1000 * mult_posw, 200 * mult_posh)
            display.blit(tutorialbox,tutorial_image)
            
            # Desenha o timer na tela em tempo real
            tempo_correndo = int(get_time())
            box_font_timer = font_timer.render(str(tempo_correndo), True,branco)
            display.blit(box_font_timer,(800*mult_posw,300*mult_posh))

            if draw_derrota:
                draw_teladerrota(tentativas,palavra_sorteada,font_roboto,font_roboto2,estrela_branca)

            # Desenha o tempo de segundos que demorou
            if draw_vitoria:
                draw_tempovitoria(font_timer,tempo_vitoria)
                draw_telavitoria(tempo_vitoria,tentativas,palavra_sorteada,font_roboto,font_roboto2,estrela_branca,estrela_azul)
                
                tela_vitoria_fontexit = font_roboto.render(str("Menu"),True,(corletra))
                botao_menu = pygame.draw.rect(display,(125,241,245),(546*mult_posw,538*mult_posh,240*mult_tam,78*mult_tam),border_radius=10)
                display.blit(tela_vitoria_fontexit,(botao_menu.x+70,botao_menu.y+10))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if botao_menu.collidepoint(mouse_pos):
                        #ranking.append((player_name, tempo_vitoria))
                        return #tempo_vitoria
                
            if tentativas == 6:
                    draw_derrota = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        return


            pygame.display.update()
            
    pygame.quit()



