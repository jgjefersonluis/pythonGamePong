import pygame
pygame.init()

# tela tamanho
display = pygame.display.set_mode((1280, 720))

# variaveis
player1 = pygame.Rect(0, 0, 30, 150)
player1_speed = 1

player2 = pygame.Rect(1250, 0, 30, 150)

ball = pygame.Rect(600, 350, 15, 15)
ball_dir_x = 1
ball_dir_y = 1


# lógica de repetição e decisão
loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed = 1
            elif event.key == pygame.K_s:
                player1_speed = 1

    # colisões
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dir_x *= -1
        hit = pygame.mixer.Sound("assets/pong.wav")
        hit.play()

    if player1.y <= 0:
        player1.y = 0
    elif player1.y >= 720 - 150:
        player1.y = 720 - 150

    player1.y += player1_speed

    if ball.x <= 0:
        ball.x = 600
        ball_dir_x *= -1
    elif ball.x >= 1280:
        ball.x = 600
        ball_dir_x *= -1

    if ball.y <= 0:
        ball_dir_x *= -1
    elif ball.y >= 720 - 15:
        ball_dir_y *= -1

    ball.x += ball_dir_x
    ball.y += ball_dir_y

    player2.y = ball.y - 75

    if player2.y <= 0:
        player2.y = 0
    elif player2.y >= 720 - 150:
        player2.y = 720 - 150

    # mostra na tela
    display.fill((0, 0, 0))
    pygame.draw.rect(display, "white", player1)
    pygame.draw.rect(display, "white", player2)
    pygame.draw.circle(display, "white", ball.center, 8)
    pygame.display.flip()
