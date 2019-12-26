import math
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 700))
background = pygame.image.load('images/background.png')
pygame.display.set_caption("GT")

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10
# Player
playerImg = pygame.image.load('images/player.png')
playerX = 180
playerY = 580
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = 1
num_of_enemies = 1


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/egg.png'))
    enemyX.append(random.randint(0, 450))
    enemyY.append(random.randint(50, 150))
    



# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 24)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (180, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
    

def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 40:
        return True
    else:
        return False

#Vòng lặp
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
           

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

   #Giới hạn di chuyển 
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 450:
        playerX = 450

    # Enemy Movement
    for i in range(num_of_enemies):
        enemyY[i] += enemyY_change


        # Collision
        collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
        if collision == True:
            score_value += 1
            enemyX[i] = random.randint(0, 450)
            enemyY[i] = random.randint(50, 150)
        if score_value > 3:
            enemyY_change = 2
        if score_value > 6:
            enemyY_change = 3
        if score_value > 15:
            enemyY_change = 4
            

        if collision == False and enemyY[i] > 580:
            score_value -= 2
            enemyX[i] = random.randint(0, 450)
            enemyY[i] = random.randint(50, 150)
        if score_value < 0:
            game_over_text()
            break
        enemy(enemyX[i], enemyY[i], i)
		
		
    
    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
