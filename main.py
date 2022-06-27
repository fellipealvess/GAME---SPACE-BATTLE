import pygame
import os
from pygame.locals import*
pygame.init
pygame.font.init()
pygame.mixer.init()

tela_largura = 900
tela_altura = 500
largura_nave = 60
altura_nave = 42

som_colisao = pygame.mixer.sound(os.path.join('sons', 'col.mp3'))
som_disparo = pygame.mixer.sound(os.path.join('sons', 'disparo.mp3'))

fundo = pygame.image.load('imgs/fundodojogo.jpg')
player1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'player1.png')),
                                          (largura_nave, altura_nave)), 90)


tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption(" SPACE WAR ")
fps = pygame.time.Clock()


jogo_aberto = True
while jogo_aberto:
    fps.tick(60)
    tela.blit(fundo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_aberto = False
    tela.blit(player1, (100, 50))




    pygame.draw.rect(tela,(0, 0, 0), ((tela_largura//2 - 5), 0, 10, tela_altura)) #linha pra dividir a tela
    pygame.display.update()
pygame.quit()

