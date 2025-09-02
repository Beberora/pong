import random

def ballPaddleReset(ball_x, ball_y, right_paddle_y, left_paddle_y):
     ball_x = width//2
     ball_y = height//2
     left_paddle_y = height//2
     right_paddle_y = height//2
        
def ballDirection(paddle_y, ball_y):
    if paddle_y == ball_y:
        return 1
    elif abs(paddle_y+1) == ball_y:
        return 2
    elif abs(paddle_y+2) == ball_y:
        return 3
    
def printGreetings():
    print("Добро пожаловать в Pong")
    roundsNumber = int(input('Введите количество раундов: '))
    return roundsNumber

width = 80  # ширина поля
height = 25  # высота поля
paddleHeight = 3  # высота ракетки
left_paddle_x = 1  # x-позиция левой ракетки (фиксирована у левой стенки)
right_paddle_x = width - 2  # x-позиция правой ракетки (фиксирована у правой стенки)

def printField(leftPaddleY, rightPaddleY, leftPaddleX, rightPaddleX, ballX, ballY, firstUserPoints,secondUserPoints):
    field = []

    topBorder = '+' + '-' * (width - 2) + '+'
    field.append(topBorder)

    for y in range(1, height -1):
        rowChars = []
        for x in range(width):
            if x == 0:
                rowChars.append('|')
            elif x == width -1:
                rowChars.append('|')
            elif x == leftPaddleX and leftPaddleY <= y < leftPaddleY + paddleHeight:
                rowChars.append('|')
            elif x == rightPaddleX and rightPaddleY <= y < rightPaddleY + paddleHeight:
                rowChars.append('|')
            elif x == ballX and y == ballY:
                rowChars.append('o')
            else:
                rowChars.append(' ')
        field.append(''.join(rowChars))

    bottomBorder = '+' + '-' * (width - 2) + '+'
    field.append(bottomBorder)
    usersScore = ' ' * (width//2-3) + str(firstUserPoints) + ' : ' + str(secondUserPoints)
    field.append(usersScore)

    for line in field:
        print(line)




firstUserPoints = 0
secondUserPoints = 0
roundsNumber = printGreetings()

ballDirectionPoint = -1
left_paddle_y = height // 2 - 1
right_paddle_y = height // 2 - 1
ball_x = width // 2
ball_y = height // 2

isFirstUserTurn = random.randint(0, 1)

   
while roundsNumber != firstUserPoints + secondUserPoints:
    printField(left_paddle_y, right_paddle_y, left_paddle_x, right_paddle_x, ball_x, ball_y, firstUserPoints, secondUserPoints)
    userTurn = input('Ваш ход: ')
    if userTurn != 'z' and userTurn != 'a' and userTurn != 'm' and userTurn != 'k':
        print("Неккоректный ввод")
    
    elif left_paddle_y != 21 and userTurn == 'z':    
        left_paddle_y += 1
            
    elif left_paddle_y != 1 and userTurn == 'a':
        left_paddle_y -= 1
            
    elif right_paddle_y != 21 and userTurn == 'm':
        right_paddle_y += 1
        
    elif right_paddle_y != 1 and userTurn == 'k':
        right_paddle_y -= 1

    if ball_y == height-1:
        ballDirectionPoint = 1
    elif ball_y == 1:
        ballDirectionPoint = 3
        
    if abs(left_paddle_x - ball_x) == 1 and ball_y >= left_paddle_y and ball_y <= left_paddle_y+2:  
        ballDirectionPoint = ballDirection(left_paddle_y, ball_y)
        isFirstUserTurn = 0     

    elif abs(right_paddle_x - ball_x) == 1 and ball_y >= right_paddle_y and ball_y <= right_paddle_y+2:
        ballDirectionPoint = ballDirection(right_paddle_y, ball_y)
        isFirstUserTurn = 1
    
    if isFirstUserTurn == 1:
        ball_x -= 1
    else:
        ball_x += 1
        
    if ballDirectionPoint == 1:
        ball_y -= 1
    elif ballDirectionPoint == 3:
        ball_y += 1

    if left_paddle_x == ball_x:
        secondUserPoints += 1
        ballPaddleReset(ball_x, ball_y, right_paddle_y, left_paddle_y)
        
    if right_paddle_x == ball_x:
        firstUserPoints += 1
        ballPaddleReset(ball_x, ball_y, right_paddle_y, left_paddle_y)

if secondUserPoints > firstUserPoints:
    print("Победил второй игрок со счетом", firstUserPoints, ":", secondUserPoints)
elif secondUserPoints < firstUserPoints:
    print("Победил первый игрок со счетом", firstUserPoints, ":", secondUserPoints)
else:
    print("Победила дружба со счетом", firstUserPoints, ":", secondUserPoints)
    
