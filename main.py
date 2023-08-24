import pygame

pygame.init()
pygame.font.init()
# tela tamanho
display = pygame.display.set_mode((1280, 720))
# variaveis
player1 = pygame.Rect(0, 0, 30, 150)
player1_score = 0
player1_speed = 1

player2 = pygame.Rect(1250, 0, 30, 150)
player2_score = 0

ball = pygame.Rect(600, 350, 15, 15)
ball_dir_x = 1
ball_dir_y = 1

font = pygame.font.Font(None, 50)
placar_player1 = font.render(str(player1_score), True, "white")
placar_player2 = font.render(str(player2_score), True, "white")

# lógica de repetição e decisão
loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed = -1
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
        player2_score += 1
        placar_player2 = font.render(str(player2_score), True, "white")
        ball.x = 600
        ball_dir_x *= -1
    elif ball.x >= 1280:
        player1_score += 1
        placar_player1 = font.render(str(player1_score), True, "white")
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
    display.blit(placar_player1, (500, 50))
    display.blit(placar_player2, (780, 50))
    pygame.display.flip()
