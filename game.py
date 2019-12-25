import math
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 700))
background = pygame.image.load('images/background.png')
pygame.display.set_caption("GT")



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
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0, 350))
    enemyY.append(random.randint(50, 150))




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



running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
           

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

   #Giới hạn di chuyển 
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 350:
        playerX = 350

    # Enemy Movement
    for i in range(num_of_enemies):
        enemyY[i] += enemyY_change


        # Collision
        collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
        if collision == True:
            enemyX[i] = random.randint(0, 350)
            enemyY[i] = random.randint(50, 150)
			
        enemy(enemyX[i], enemyY[i], i)
		
		
    
    player(playerX, playerY)
    pygame.display.update()
