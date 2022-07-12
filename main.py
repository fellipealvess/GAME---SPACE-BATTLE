import pygame
import os
from pygame.locals import *

pygame.init
pygame.font.init()
pygame.mixer.init()

tela_largura = 900
tela_altura = 500
largura_nave = 60
altura_nave = 42

velocidade = 8

som_colisao = pygame.mixer.Sound(os.path.join('sons', 'col.mp3'))
som_disparo = pygame.mixer.Sound(os.path.join('sons', 'disparo.mp3'))

fundo = pygame.image.load('imgs/fundodojogo.jpg')
player1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'player1.png')),
                                                         (largura_nave, altura_nave)), 90)
player2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'player2.png')),
                                                         (largura_nave, altura_nave)), 90)
tela = pygame.display.set_mode((tela_largura, tela_altura))
p2 = pygame.Rect(700, 300, largura_nave, altura_nave)
p1 = pygame.Rect(100, 300, largura_nave, altura_nave)


def naves(p1 ,p2):
    tela.blit(player1, (p1.x, p1.y))
    tela.blit(player2, (p2.x, p2.y))

def movimentacao_p1(tecla ,p1):
    if tecla[pygame.K_a] and p1.x - velocidade > 0:  #esquerda
        p1.x += -velocidade
    if tecla[pygame.K_s] and p1.y + velocidade + p1.height + 5 < (tela_altura):  #baixo
        p1.y += velocidade
    if tecla[pygame.K_d] and p1.x + velocidade + p1.width - 15 < (tela_largura/2 - 5):  #direita
        p1.x += velocidade
    if tecla[pygame.K_w] and p1.y + velocidade - 8 > 0:  #cima
        p1.y += -velocidade

def movimentacao_p2(tecla, p2):
    if tecla[pygame.K_LEFT] and p2.x - velocidade > (tela_largura//2 - 5): #esquerda
        p2.x += -velocidade
    if tecla[pygame.K_DOWN] and p2.y + velocidade + p2.height + 15 < tela_altura:  #baixo
        p2.y += velocidade
    if tecla[pygame.K_RIGHT] and p2.x + velocidade + p2.width - 20 < tela_largura: #direita
        p2.x += velocidade
    if tecla[pygame.K_UP] and p2.y + velocidade - 8 > 0:  #cima
        p2.y += -velocidade


pygame.display.set_caption(" Space Battle ")
fps = pygame.time.Clock()

jogo_aberto = True
while jogo_aberto:
    fps.tick(60)
    tela.blit(fundo, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_aberto = False
    tela.blit(player1, (p1.x, p1.y))
    tela.blit(player2, (p2.x, p2.y))
    naves(p1, p2)
    tecla = pygame.key.get_pressed()
    movimentacao_p1(tecla, p1)
    movimentacao_p2(tecla, p2)

    pygame.draw.rect(tela, (0, 0, 0), ((tela_largura//2 - 5), 0, 10, tela_altura)) # linha pra dividir a tela
    pygame.display.update()
pygame.quit()
