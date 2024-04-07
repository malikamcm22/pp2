import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)  # Создаем экран с заданными размерами
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

paddleW = 150  # Ширина ракетки
paddleH = 25   # Высота ракетки
paddleSpeed = 20  # Скорость перемещения ракетки
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)  # Создаем прямоугольник для ракетки

ballRadius = 20  # Радиус мяча
ballSpeed = 6    # Скорость мяча
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)  # Создаем прямоугольник для мяча
dx, dy = 1, -1  # Направление движения мяча по осям x и y

game_score = 0  # Счет игры
game_score_fonts = pygame.font.SysFont('comicsansms', 40)  # Создаем шрифт для отображения счета
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))  # Создаем текст счета
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

collision_sound = pygame.mixer.Sound('catch.mp3')  # Звук столкновения мяча с объектом

def detect_collision(dx, dy, ball, rect):
    """Функция для обнаружения столкновения мяча с прямоугольным объектом."""
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]  # Создаем список блоков
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)]  # Создаем список цветов для блоков

losefont = pygame.font.SysFont('comicsansms', 40)  # Создаем шрифт для сообщения о проигрыше
losetext = losefont.render('Game Over', True, (255, 255, 255))  # Создаем текст для сообщения о проигрыше
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

winfont = pygame.font.SysFont('comicsansms', 40)  # Создаем шрифт для сообщения о победе
wintext = losefont.render('You win yay', True, (0, 0, 0))  # Создаем текст для сообщения о победе
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

paused = False  # Флаг паузы игры

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:  # Проверка нажатия на клавишу "P" для паузы
            paused = not paused  # Инвертируем значение флага паузы

    if not paused:  # Если игра не на паузе
        screen.fill(bg)  # Заливаем экран цветом фона

        [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]  # Рисуем блоки
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)  # Рисуем ракетку
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)  # Рисуем мяч

        ball.x += ballSpeed * dx  # Двигаем мяч по горизонтали
        ball.y += ballSpeed * dy  # Двигаем мяч по вертикали

        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:  # Проверка столкновения мяча с границами экрана
            dx = -dx
        if ball.centery < ballRadius + 50: 
            dy = -dy
        if ball.colliderect(paddle) and dy > 0:  # Проверка столкновения мяча с ракеткой
            dx, dy = detect_collision(dx, dy, ball, paddle)

        hitIndex = ball.collidelist(block_list)  # Проверка столкновения мяча с блоками

        if hitIndex != -1:  # Если мяч столкнулся с блоком
            hitRect = block_list.pop(hitIndex)  # Удаляем блок из списка
            hitColor = color_list.pop(hitIndex)  # Удаляем цвет блока из списка цветов
            dx, dy = detect_collision(dx, dy, ball, hitRect)  # Вызываем функцию для определения направления отскока мяча
            game_score += 1  # Увеличиваем счетчик очков
            collision_sound.play()  # Воспроизводим звук столкновения

        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)  # Отображаем счет игры на экране

        if ball.bottom > H:  # Если мяч вышел за нижнюю границу экрана
            screen.fill((0, 0, 0))  # Заливаем экран цветом фона
            screen.blit(losetext, losetextRect)  # Отображаем текст "Game Over"
        elif not len(block_list):  # Если все блоки разрушены
            screen.fill((255,255, 255))  # Заливаем экран белым цветом
            screen.blit(wintext, wintextRect)  # Отображаем текст "You win yay"

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:  # Проверка нажатия клавиши "Влево" и столкновения с левой границей экрана
            paddle.left -= paddleSpeed  # Перемещаем ракетку влево
        if key[pygame.K_RIGHT] and paddle.right < W:  # Проверка нажатия клавиши "Вправо" и столкновения с правой границей экрана
            paddle.right += paddleSpeed  # Перемещаем ракетку вправо

    pygame.display.flip()
    clock.tick(FPS)