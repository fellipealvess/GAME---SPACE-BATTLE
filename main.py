mport pygame
import os
pygame.font.init()
pygame.mixer.init()

tela_altura = 500
tela_largura = 900
largura_nave = 60
altura_nave = 42
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Space Battle")

velocidade_nave = 5
velocidade_bala = 7
max_bala = 5

som_colisao = pygame.mixer.Sound(os.path.join('sons', 'col.mp3'))
som_disparo = pygame.mixer.Sound(os.path.join('sons', 'disparo.mp3'))

fonte_health_points = pygame.font.SysFont('comicsans', 40)
fonte_winner = pygame.font.SysFont('comicsans', 50)


fundo = pygame.image.load('imgs/fundodojogo.jpg')
player1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'player1.png')),
                                                         (largura_nave, altura_nave)), 90)
player2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'player2.png')),
                                                         (75, 52)), 90)
p2 = pygame.Rect(700, 300, largura_nave, altura_nave)
p1 = pygame.Rect(100, 300, largura_nave, altura_nave)

p1_acerto = pygame.USEREVENT + 1
p2_acerto = pygame.USEREVENT + 2

p1_municao = []
p2_municao = []

p2_hp = 10
p1_hp = 10
fps = 60

def municao_hp(p2, p1, p2_municao, p1_municao, p2_hp, p1_hp):
    p2_hp_texto = fonte_health_points.render("HP: " + str(p2_hp), 1, (255,255,255))
    p1_hp_texto = fonte_health_points.render("HP: " + str(p1_hp), 1, (255,255,255))
    tela.blit(p2_hp_texto, (tela_largura - p2_hp_texto.get_width() - 10, 10))
    tela.blit(p1_hp_texto, (10, 10))

    tela.blit(player1, (p1.x, p1.y))
    tela.blit(player2, (p2.x, p2.y))

    for bullet2 in p2_municao:
        pygame.draw.rect(tela, (0,100,0), bullet2)

    for bullet in p1_municao:
        pygame.draw.rect(tela, (128,128,128), bullet)

    pygame.display.update()


def movimentacao_p1(tecla ,p1):
    if tecla[pygame.K_a] and p1.x - velocidade_nave > 0:  #esquerda
        p1.x += -velocidade_nave
    if tecla[pygame.K_s] and p1.y + velocidade_nave + p1.height + 5 < (tela_altura):  #baixo
        p1.y += velocidade_nave
    if tecla[pygame.K_d] and p1.x + velocidade_nave + p1.width - 15 < (tela_largura/2 - 5):  #direita
        p1.x += velocidade_nave
    if tecla[pygame.K_w] and p1.y + velocidade_nave - 8 > 0:  #cima
        p1.y += -velocidade_nave


def movimentacao_p2(tecla, p2):
    if tecla[pygame.K_LEFT] and p2.x - velocidade_nave > (tela_largura//2 - 5): #esquerda
        p2.x += -velocidade_nave
    if tecla[pygame.K_DOWN] and p2.y + velocidade_nave + p2.height + 15 < tela_altura:  #baixo
        p2.y += velocidade_nave
    if tecla[pygame.K_RIGHT] and p2.x + velocidade_nave + p2.width - 20 < tela_largura: #direita
        p2.x += velocidade_nave
    if tecla[pygame.K_UP] and p2.y + velocidade_nave - 8 > 0:  #cima
        p2.y += -velocidade_nave


def lista_balas(p1_municao, p2_municao,p2,p1):
    for bullet in p1_municao:
        bullet.x += velocidade_bala
        if p2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(p2_acerto))
            p1_municao.remove(bullet)
        elif bullet.x > tela_largura:
            p1_municao.remove(bullet)

    for bullet in p2_municao:
        bullet.x -= velocidade_bala
        if p1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(p1_acerto))
            p2_municao.remove(bullet)
        elif bullet.x < 0:
            p2_municao.remove(bullet)


def tela_winner(text):
    draw_text = fonte_winner.render(text, 1, (255,255,255))
    tela.blit(draw_text, (tela_altura/2 - draw_text.get_width()/2, tela_altura/2 - draw_text.get_height()))
    pygame.display.update()
    pygame.time.delay(5000)

clock = pygame.time.Clock()
run = True
while run:
    tela.blit(fundo, (0, 0))
    pygame.draw.rect(tela, (0, 0, 0), ((tela_largura//2 - 5), 0, 10, tela_altura)) # linha pra dividir a tela
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(p1_municao) < max_bala:
                bullet = pygame.Rect(p1.x + p1.width, p1.y + p1.height /2, 8, 5)
                p1_municao.append(bullet)
                som_disparo.play()
            if event.key == pygame.K_KP_ENTER and len(p2_municao) < max_bala:
                bullet = pygame.Rect(p2.x, p2.y + p2.height /2, 8, 5)
                p2_municao.append(bullet)
                som_disparo.play()

        if event.type == p2_acerto:
            p2_hp -= 1
            som_colisao.play()
        if event.type == p1_acerto:
            p1_hp -= 1
            som_colisao.play()

    winner_text = ""
    if p2_hp <= 0:
        winner_text = "Player 1 Wins!"
    if p1_hp <= 0:
        winner_text = "Player 2 Wins!"

    if winner_text != "":
        tela_winner(winner_text)
        break

    tecla = pygame.key.get_pressed()

    movimentacao_p1(tecla, p1)

    movimentacao_p2(tecla, p2)

    lista_balas(p1_municao, p2_municao, p2, p1)

    municao_hp(p2, p1, p2_municao, p1_municao, p2_hp, p1_hp)

