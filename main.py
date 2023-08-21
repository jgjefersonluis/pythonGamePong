import pygame

# tela tamanho
display = pygame.display.set_mode((1280, 720))

# variaveis
player1 = pygame.Rect(0, 0, 30, 150)
player2 = pygame.Rect(1250, 0, 30, 150)
ball = pygame.Rect(600, 350, 15, 15)

# lógica de repetição e decisão
loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                loop = False

    # mostra na tela
    display.fill((0,0,0))
    pygame.draw.rect(display, "white", player1)
    pygame.draw.rect(display, "white", player2)
    pygame.draw.circle(display, "white", ball.center, 8)
    pygame.display.flip()
