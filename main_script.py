import pygame
import random
import math

# INITIALIZING THE PYGAME MODULE
pygame.init()

# SETTING THE WINDOW SIZE
window = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Playboi Life")

# DECLARING PLAYER IMAGE AND LOCATION
playerImg = pygame.image.load("people.png")
playerX = 20
playerY = 298
screen_width = 1000
screen_height = 650

# SPEED OF THE PLAYER AND THE HEARTS/ENEMY
speed = 0.5
speed_heart = 1
speed_plus = 1

# TOTAL POINTS [GAME]
total_points = 0

# "TOTAL" TEXT ON THE TOP LEFT CORNER IN THE SCREEN
font = pygame.font.Font("freesansbold.ttf", 20)
fontX = 10
fontY = 10

# "LIVES" TEXT ON THE TOP RIGHT CORNER IN THE SCREEN
livesX = 900
livesY = 10

# TOTAL LIVES BEFORE GAME OVER
total_lives = 3

# LEVEL UPS FOR SCORING POINTS
levelUpImg = pygame.image.load("plus.png")
levelUpX = random.randint(800, 1000)
levelUpY = random.randint(0, 650)

##### CODE ON SETTING THE HEART NAME(S), COORDINATE(S)
heartImg = []
heartX = []
heartY = []

total_number_of_enemies = 2

for number in range(total_number_of_enemies):
    heartImg.append(pygame.image.load("candle.png"))
    heartX.append(random.randint(800, 1000))
    heartY.append(random.randint(0, 650))

##### GAME OVER SCREEN ######
game_over = pygame.font.Font("freesansbold.ttf", 20)
game_overX = 450
game_overY = 290

you_win = pygame.font.Font("freesansbold.ttf", 20)

you_lose = pygame.font.Font("freesansbold.ttf", 20)

# GAME FUNCTIONS

def player(x, y):
    window.blit(playerImg, (x, y))

def heart(x, y, z):
    window.blit(heartImg[z], (x, y))

def level(x, y):
    window.blit(levelUpImg, (x, y))

def isCollision(playerX, playerY, heartX, heartY):
    distance = math.sqrt(math.pow(playerX - heartX,2) + math.pow(playerY - heartY,2))
    if distance < 29:
        return True
    else:
        return False

def points(x,y):
    points = font.render(f"Total: {total_points}", True, (255, 255, 255))
    window.blit(points, (x, y))

def lives(x,y):
    live = font.render(f"Lives: {total_lives}", True, (255, 255, 255))
    window.blit(live, (x, y))

def win(x,y):
    gameover = font.render("YOU WIN", True, (255, 255, 255))
    window.blit(gameover, (x, y))

def lose(x,y):
    gameover = font.render("YOU LOSE", True, (255, 255, 255))
    window.blit(gameover, (x, y))


# WHILE THE SCREEN IS ON/RUNNING
screen_on = True
while screen_on:

    window.fill((155, 25, 80))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_on = False

    # KEY STROKES FOR PLAYER MOVEMENT
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerX != 0:
        playerX -= speed
    if keys[pygame.K_RIGHT] and playerX != screen_width - 68:
        playerX += speed
    if keys[pygame.K_UP] and playerY != 0:
        playerY -= speed
    if keys[pygame.K_DOWN] and playerY != screen_height - 68:
        playerY += speed
    player(playerX, playerY)

    # ENEMY/HEARTS MOVEMENT CODE
    for index in range(total_number_of_enemies):

        if total_lives == 0:
            for number in range(total_number_of_enemies):
                heartY = 2000
            lose(game_overX, game_overY)
            break
        if total_points == 10:
            for number in range(total_number_of_enemies):
                heartY = 2000
            win(game_overX, game_overY)
            break

        heartX[index] -= speed_heart
        if heartX[index] <= 0:
            heartX[index] = random.randint(800, 1000)
            heartY[index] = random.randint(0, 600)
            if speed_heart <= 2.5:
                speed_heart += 0.25
            else:
                speed_heart +=0

        # INCASE OF COLLISIONS
        collision = isCollision(playerX, playerY, heartX[index], heartY[index])
        if collision:
            heartX[index] = random.randint(800, 1000)
            heartY[index] = random.randint(0, 600)
            total_lives -= 1
        heart(heartX[index], heartY[index], index)

    if total_lives == 0:
        levelUpY = 2000
        lose(game_overX, game_overY)
    if total_points == 10:
        levelUpY = 2000
        win(game_overX, game_overY)

    # LEVEL UP MOVEMENTS
    levelUpX -= speed_plus
    if levelUpX <= 0:
        levelUpX = random.randint(800, 1000)
        levelUpY = random.randint(0, 600)

    # COLLISION WITH LEVEL UPS
    collision = isCollision(playerX, playerY, levelUpX, levelUpY)
    if collision:
        levelUpX = random.randint(800, 1000)
        levelUpY = random.randint(0, 600)
        total_points += 1

    # CALLING THE FUNCTIONS
    points(fontX, fontY)
    lives(livesX, livesY)
    level(levelUpX, levelUpY)
    pygame.display.update()


# GAME DONE