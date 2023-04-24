import pygame

# Inicjacja Pygame
pygame.init()

# Ustawienia okna
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pong')

# Kolory
white = (255, 255, 255)
black = (0, 0, 0)

# Wymiary paletki
paddle_width = 15
paddle_height = 60

# Wymiary piłki
ball_width = 15
ball_height = 15

# Prędkość paletki
paddle_speed = 5

# Prędkość piłki
ball_x_speed = 6
ball_y_speed = 6

# Ustawienie zegara
clock = pygame.time.Clock()
framerate = 45

# Inicjacja paletki gracza
player_paddle_x = 25
player_paddle_y = (window_height - paddle_height) / 2

# Inicjacja paletki przeciwnika
opponent_paddle_x = window_width - paddle_width - 25
opponent_paddle_y = (window_height - paddle_height) / 2

# Inicjacja piłki
ball_x = window_width / 2
ball_y = window_height / 2

# Punkty gracza i przeciwnika
player_score = 0
opponent_score = 0

# Czcionka i rozmiar tekstu
font = pygame.font.Font(None, 36)

pygame.mixer.init() # Inicjalizacja modułu mixer
pygame.mixer.music.load('giera.mp3') # Wczytanie pliku muzyki
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play() # Odtworzenie muzyki

# Dźwięk odbijania piłki

bounce_sound = pygame.mixer.Sound('Smash.mp3')
score_sound = pygame.mixer.Sound('beeep.mp3')

# Załadowanie tła
background = pygame.image.load("Droga_Mleczna.jpg")

# Pętla gry
while True:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    # Rysowanie tła
    window.blit(background, (0, 0))

    # Rysowanie paletki gracza
    pygame.draw.rect(window, white, (player_paddle_x, player_paddle_y, paddle_width, paddle_height))

    # Rysowanie paletki przeciwnika
    pygame.draw.rect(window, white, (opponent_paddle_x, opponent_paddle_y, paddle_width, paddle_height))

    # Rysowanie piłki
    pygame.draw.rect(window, white, (ball_x, ball_y, ball_width, ball_height))

    # Rysowanie linii środkowej
    pygame.draw.line(window, white, (window_width/2, 0), (window_width/2, window_height))

    # Obsługa ruchu paletki gracza
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle_y > 0:
        player_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle_y < window_height - paddle_height:
        player_paddle_y += paddle_speed

    # Obsługa ruchu paletki przeciwnika
    if opponent_paddle_y + paddle_height/2 < ball_y:
        opponent_paddle_y += paddle_speed
    elif opponent_paddle_y + paddle_height/2 > ball_y:
        opponent_paddle_y -= paddle_speed

    # Obsługa ruchu piłki
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Odbicie piłki od paletki gracza
    if ball_x <= player_paddle_x + paddle_width and ball_y >= player_paddle_y and ball_y <= player_paddle_y + paddle_height:
        ball_x_speed = -ball_x_speed
        bounce_sound.play()

    # Odbicie piłki od paletki przeciwnika
    if ball_x >= opponent_paddle_x - ball_width and ball_y >= opponent_paddle_y and ball_y <= opponent_paddle_y + paddle_height:
        ball_x_speed = -ball_x_speed
        bounce_sound.play()

    # Odbicie piłki od ściany górnej i dolnej
    if ball_y <= 0 or ball_y >= window_height - ball_height:
        ball_y_speed = -ball_y_speed
        bounce_sound.play()

    # Punkty gracza i przeciwnika
    if ball_x <= 0:
        opponent_score += 1
        ball_x = window_width / 2
        ball_y = window_height / 2
        ball_x_speed = -ball_x_speed
        score_sound.play()
        score_sound.play()
    elif ball_x >= window_width - ball_width:
        player_score += 1
        ball_x = window_width / 2
        ball_y = window_height / 2
        ball_x_speed = -ball_x_speed
        score_sound.play()

    # Rysowanie wyników
    player_score_text = font.render(str(player_score), True, white)
    opponent_score_text = font.render(str(opponent_score), True, white)
    window.blit(player_score_text, (window_width / 2 - 50, 10))
    window.blit(opponent_score_text, (window_width / 2 + 25, 10))

    # Sprawdzanie warunku zwycięstwa
    if player_score == 10:
        winner_text = font.render("Gracz wygrywa!", True, white)
        window.blit(winner_text, (window_width / 2 - 75, window_height / 2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()
    if opponent_score == 10:
        winner_text = font.render("Przeciwnik wygrywa!", True, white)
        window.blit(winner_text, (window_width / 2 - 95, window_height / 2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()

    # Aktualizacja ekranu
    pygame.display.update()

    # Zwolnienie tempa gry
    clock.tick(framerate)


