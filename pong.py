def printGreetings():
    print("Добро пожаловать в Pong")
    roundsNumber = int(input('Введите количество раундов:'))
    return roundsNumber

def printField(left_paddle_y, right_paddle_y, ball_x, ball_y):
    # Отрисовка поля с фиксированными параметрами
    field = []
    
    width = 80  # ширина поля
    height = 24  # высота поля
    paddleHeight = 3  # высота ракетки
    left_paddle_x = 1  # x-позиция левой ракетки (фиксирована у левой стенки)
    right_paddle_x = width - 2  # x-позиция правой ракетки (фиксирована у правой стенки)
     
    top_border = '+' + '-' * (width - 2) + '+'
    field.append(top_border)

    for y in range(1, height - 1):
        row_chars = []
        for x in range(width):
            if x == 0:
                row_chars.append('|')
            elif x == width - 1:
                row_chars.append('|')
            elif x == left_paddle_x and left_paddle_y <= y < left_paddle_y + paddleHeight:
                row_chars.append('|')
            elif x == right_paddle_x and right_paddle_y <= y < right_paddle_y + paddleHeight:
                row_chars.append('|')
            elif x == ball_x and y == ball_y:
                row_chars.append('o')
            else:
                row_chars.append(' ')
        field.append(''.join(row_chars))

    bottom_border = '+' + '-' * (width - 2) + '+'
    field.append(bottom_border)

    # Печать поля
    for line in field:
        print(line)



firstUserPoints = 0
secondUserPoints = 0
roundsNumber = printGreetings()

left_paddle_y = height // 2
right_paddle_y = height // 2
ball_x = width // 2
ball_y = height // 2
    
while roundsNumber != firstUserPoints + secondUserPoints:
