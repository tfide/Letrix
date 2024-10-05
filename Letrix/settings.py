import pygame
import os


branco = (255,255,255)
corcorreta = (125, 241, 245)
corerrada = (191, 191, 191)
corneutra = (81, 111, 148)
corletra = (36, 36, 36)
corfundo =(35,35,35)

x_cordenada = 110  # Coordenada inicial X
y_cordenada = 0


temas = {
    'Animais': ['cabra'],
}
temas4 = {
    'Anima': ['mula'],
}

pygame.init()
info_tela = pygame.display.Info()
wdisplay = 1920
hdisplay = 1080


# valor 1.45 para resulução 1920, 1080  = fullhd
mult_posw = 1.45
mult_posh = 1.45
mult_tam = 1.45

display = pygame.display.set_mode([wdisplay,hdisplay])

blur_surf = pygame.Surface((wdisplay,hdisplay))
blur_surf.set_alpha(200)  # Ajuste o nível de transparência (0 a 255)
blur_surf.fill((0, 0, 0))  # Cor de preenchimento do embaçamento (preto com transparência)

# Diretorio das musicas
music_directory = "./assets/music/" 
playlist = [os.path.join(music_directory, file) for file in os.listdir(music_directory) if file.endswith(('.mp3', '.wav'))] 
#Usando a biblioteca "os" em um for para identificar todas as musicas sem precisar digitar todas em uma lista





