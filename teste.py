import pygame
pygame.init()

largura = 800
altura = 500
x = largura/2
y = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(" ??? ")
fps = pygame.time.Clock()

jogo_aberto = True
while jogo_aberto:
    fps.tick(70)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_aberto = False
    pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 50))
    if y >= altura:
        y = 0
    y += 1
    pygame.display.update()
pygame.quit()









