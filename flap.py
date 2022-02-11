import pygame
import random

pygame.init()

#screen size
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("C:/Users/Krishna Murugan/Documents/flappybird/background.png")

#changing the name and the icon of the game
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("C:/Users/Krishna Murugan/Documents/flappybird/aeroplane.jpg")
pygame.display.set_icon(icon)

#making flappy bird appear
Flappy_Bird = pygame.image.load("C:/Users/Krishna Murugan/Documents/flappybird/bird2.png")
birdX = 200
birdY = 250
birdY_change = 0


#making the pipes
pipe_width = 70
pipe_height = random.randint(150,300)
pipe_colour = (11, 122, 5)
pipeX = 800
pipeX_change = -5

#score
score_value = 0

#font
def font():
    font = pygame.font.Font("C:/Users/Krishna Murugan/Documents/flappybird/FlappyBirdy.ttf",150)
    text=font.render("Game Over",True,(0,0,0))
    screen.blit(text,(220,220))

def score(score_value):
    score_font = pygame.font.Font("C:/Users/Krishna Murugan/Documents/flappybird/Justicia.ttf",50)
    score_text = score_font.render(f"Score: {score_value}",True,(0,0,0))
    screen.blit(score_text,(10,10))


def pipe_display(height): #ps
    pygame.draw.rect(screen, pipe_colour,pygame.Rect(pipeX, 0, pipe_width, height)) #ps
    bottom_pipe_height = height + 150 #ps
    bottom_height = 485-bottom_pipe_height #ps
    pygame.draw.rect(screen, pipe_colour,pygame.Rect(pipeX, bottom_pipe_height, pipe_width, bottom_height)) #ps

def player(x,y):
    screen.blit(Flappy_Bird , (x,y))

#collision
def collision(pipeX, pipe_height, birdY, bottom_height): #PS
    if pipeX >= 50 and pipeX <= (50+64): 
        if birdY<pipe_height or birdY+50>bottom_height:
                return True
        return False

# START SCREEN
startFont = pygame.font.Font('Justicia.ttf', 32) #PS
def start():
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 87, 51))
    screen.blit(display, (130, 160))
    pygame.display.update()

score_array = [0]

game_over_font1 = pygame.font.Font('FlappyBirdy.ttf', 200)
game_over_font2 = pygame.font.Font('Justicia.ttf', 32)

def game_over(): #PS
    # check for the maximum score
    maximum = max(score_array)
    #  "game over"
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    screen.blit(display1, (130, 250))
    # shows your current score and your max score
    display2 = game_over_font2.render(f"SCORE : {score_value} MAX SCORE : {maximum}", True, (116, 51, 255))
    screen.blit(display2, (200, 400))
    #  If your new score is the same as the maximum then u reached a new high score
    if score_value == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!!", True, (200,35,35))
        screen.blit(display3, (240, 80))

#looping the screen so that the window doesn't close immediately
running = True 
waiting = True
collision_detect = False
clock = pygame.time.Clock()

while running:    
    clock.tick(60)
    screen.fill((13, 143, 148))
    screen.blit(background , (0,0))

    while waiting:
        if collision_detect:
            game_over()
            start()
        else:
            start()

#controls
        for x in pygame.event.get():
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_SPACE:
                    score_value = 0
                    birdY = 250
                    pipeX = 800
                    waiting = False

            if x.type == pygame.QUIT:
                waiting = False
                running = False
     
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            # If you press exit you exit out of the while loop and pygame quits
            running = False

        if x.type == pygame.KEYDOWN:
            if x.key == pygame.K_SPACE:
                #  if you press spacebar you will move up
                birdY_change = -6
        
        if x.type == pygame.KEYUP:
            if x.key == pygame.K_SPACE:
                birdY_change = 3

#boundries   
    birdY += birdY_change
    if birdY <= 0:
        birdY = 0
    if birdY >= 432 :
        birdY = 432

    pipeX += pipeX_change

    collision_detect = collision(pipeX, pipe_height, birdY, pipe_height + 150)

    if collision_detect:
        score_array.append(score_value)
        waiting = True

    if pipeX <= -10:
        pipeX = 800
        pipe_height = random.randint(200,400)
        score_value+=1
    
    pipe_display(pipe_height)
    player(birdX,birdY)
    score(score_value)
 
    pygame.display.update()
pygame.quit()