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
    'Animais': ['cabra','tigre', 'cobra', 'zebra','aguia','cervo','furao','grilo','ponei','urubu','pavao','lebre','arara','porco','corvo','lesma','panda'],
    
    'Objetos': ['adaga', 'apito', 'album', 'balao', 'banco', 'blusa', 'boina', 'botao', 'broca', 'boina', 'buque', 'anzol', 'caixa', 'cesta', 'chave',
    'cofre', 'coifa', 'dardo', 'disco', 'facao', 'farda', 'fogao', 'fuzil', 'funil', 'gaita', 'garfo', 'gorro', 'jarra', 'jeans', 'lacre', 'lapis', 
    'lente', 'leque', 'livro', 'lousa', 'manta', 'moeda', 'mouse', 'mural', 'ofuro', 'orgao', 'papel', 'pasta', 'pedal', 'pente', 'piano', 'placa', 'porta', 
    'prato', 'radar', 'radio', 'regua', 'rifle', 'rimel', 'rolha', 'sabao', 'short', 'serra', ' spray', 'sunga', 'sutia', 'tabua', 'talco', 'tampa', 'tanga', 'telha', 
    'tenis', 'terno','tiara', 'touca', 'trave', 'trono', 'varal', 'vidro', 'viola','ziper'],
    
    'frutas':['manga','amora','cacau','caqui','limao','mamao','melao','pequi'],

    'Verbos':['achar','bolar','andar','assar','colar','atuar','errar','capar','cavar','comer','beber','tocar','mover','viver','falir','pedir','subir','trair']

}
temas4 = {
    'Animais': ['mula','alce','anta','atum','bode','boto','egua','foca','galo','gato','lobo','lula','leao','onça','orca','pato','sapo','siri','tatu','urso','vaca'],
    
    'Objetos' : ['arco', 'base', 'beca', 'boia','bola','bone', 'cabo', 'cama', 'capa', 'cera', 'chip', 'cola', 'cone', 'cruz', 'dado', 'faca', 'fita', 'gibi', 'iate', 'ioio', 'laco', 'lata',
    'leme', 'lona', 'luva', 'maca', 'maio', 'meia', 'mesa', 'mola,', 'pino', 'pipa', 'pneu', 'pote', 'rack', 'ralo',
    'rede', 'remo', 'roda', 'rodo', 'saia', 'sino', 'sofa', 'taca', 'tela', 'urna', 'vela'],

    'Frutas':['maça','caju','coco','açai','figo','kiwi','pera','jaca'],

    'Verbos':['amar','doar','miar','orar','piar','usar','roer','sair','unir','cair','doer','zoar','voar']




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

with open('./assets/ptbr.txt','r')as f:
    ptbrs = f.read().splitlines()
# Filtrar palavras com até 5 letras
palavras_ptbr = [ptbr for ptbr in ptbrs if len(ptbr) < 6]


for chave, valor in temas.items():
    for palavra in valor:
        if palavra not in palavras_ptbr:
            print(f'{chave}: {palavra}')
            palavras_ptbr.append(palavra)