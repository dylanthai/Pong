#########################################
# File Name: Pong Assignment            #
# Description: To recreate Pong         #
# Authors: Dylan and Connor             #
# Date: 11/13/2017                      #
#########################################
import pygame
from random import randint
pygame.init()
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH,HEIGHT))

RED  =(255,  0,  0)
GREEN =(  0,255,  0)
LBLUE = (173,216,230)
BLUE = (0,0,255)
WHITE =(255,255,255)
BLACK =(  0,  0,  0)
YELLOW = (255,255,0)
scoreR = 0
scoreL = 0
RightScore = "Score: "
LeftScore = "Score: "

Background = pygame.image.load("background3.jpg")
TOP = 0
BOTTOM = HEIGHT
LEFT = 0
RIGHT = WIDTH
outline = 0
#--------------------------#
# Ball Properties
#--------------------------#
ballR  = 15
ballX  = WIDTH/2
ballY  = 2*ballR
speedX = 5
speedY = 5

#-------------------------#
# Right Paddle properties
#-------------------------#
paddleRW = 20
paddleRH = 120
paddleRX= (WIDTH - paddleRW)
paddleRY = BOTTOM - paddleRH - 225
paddleRShift = 5

#------------------------#
# Left Paddle properties
#------------------------#
paddleLW = 20
paddleLH = 120
paddleLX = 0
paddleLY = BOTTOM - paddleLH - 225
paddleLShift = 5

#-----------#
# Functions #
#-----------#
#Display the Score#

def redrawgameWindow(scoreL,scoreR):
    screen.blit(Background, (0,0))
    if scoreL == 1:
        pygame.draw.line(gameWindow,LBLUE,(80,10),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(80,40),(80,70), 10)
    if scoreL == 2:
        pygame.draw.line(gameWindow,LBLUE,(50,10),(80,10), 10)
        pygame.draw.line(gameWindow,LBLUE,(80,10),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,40),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,40),(50,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,70),(80,70), 10)
    if scoreL == 3:
        pygame.draw.line(gameWindow,LBLUE,(50,10),(80,10), 10)
        pygame.draw.line(gameWindow,LBLUE,(80,10),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,40),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(80,40),(80,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,70),(80,70), 10)
    if scoreL == 4:
        pygame.draw.line(gameWindow,LBLUE,(50,10),(50,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(80,10),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,40),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(80,40),(80,70), 10)
    if scoreL == 5:
        pygame.draw.line(gameWindow,LBLUE,(50,10),(50,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,10),(80,10), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,40),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(80,40),(80,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,70),(80,70), 10)
    if scoreL == 6:
        pygame.draw.line(gameWindow,LBLUE,(50,10),(50,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,10),(80,10), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,40),(80,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,40),(50,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(80,40),(80,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(50,70),(80,70), 10)
################################################################################
    if scoreR == 1:
        pygame.draw.line(gameWindow,LBLUE,(730,10),(730,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,40),(730,70), 10)
    if scoreR == 2:
        pygame.draw.line(gameWindow,LBLUE,(750,10),(750,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,10),(750,10), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,40),(750,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,40),(730,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,70),(750,70), 10)
    if scoreR == 3:
        pygame.draw.line(gameWindow,LBLUE,(750,10),(750,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,10),(750,10), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,40),(750,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(750,40),(750,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,70),(750,70), 10)
    if scoreR == 4:
        pygame.draw.line(gameWindow,LBLUE,(750,10),(750,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,10),(730,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,40),(750,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(750,40),(750,70), 10)
    if scoreR == 5:
        pygame.draw.line(gameWindow,LBLUE,(730,10),(750,10), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,10),(730,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,40),(750,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(750,40),(750,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,70),(750,70), 10)
    if scoreR == 6:
        pygame.draw.line(gameWindow,LBLUE,(730,10),(750,10), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,10),(730,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,40),(750,40), 10)
        pygame.draw.line(gameWindow,LBLUE,(750,40),(750,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,40),(730,70), 10)
        pygame.draw.line(gameWindow,LBLUE,(730,70),(750,70), 10)
    pygame.draw.circle(gameWindow, WHITE, (ballX,ballY), ballR, outline)
    pygame.draw.rect(gameWindow, RED, (paddleLX, paddleLY, paddleLW, paddleLH), outline)
    pygame.draw.rect(gameWindow, RED, (paddleRX, paddleRY, paddleRW, paddleRH), outline)
   

# Display Time
    font = pygame.font.SysFont("",100)
    graphics = font.render(str((elapsed/1000)/60),1,LBLUE)
    gameWindow.blit(graphics,(300,10))
    font = pygame.font.SysFont("",100)
    graphics = font.render(":",1,LBLUE)
    gameWindow.blit(graphics,(334,10))
    
#Seconds
    if elapsed <60000:
        font = pygame.font.SysFont("",100)
        graphics = font.render(str(elapsed/1000),1,LBLUE)
        gameWindow.blit(graphics,(360,10))
        pygame.display.update()
    elif elapsed <70000:
        font = pygame.font.SysFont("0",100)
        graphics = font.render(str((elapsed/1000)-60),1,LBLUE)
        gameWindow.blit(graphics,(360,10))
        pygame.display.update()
    elif elapsed >70000:
        font = pygame.font.SysFont("",100)
        graphics = font.render(str((elapsed/1000)-60),1,LBLUE)
        gameWindow.blit(graphics,(360,10))
        pygame.display.update()
    elif elapsed >71000:
        font = pygame.font.SysFont("",100)
        graphics = font.render(str((elapsed/1000)-60),1,LBLUE)
        gameWindow.blit(graphics,(360,10))
        pygame.display.update()
        
# Display the end screens #
def endScreenOne(scoreL,scoreR):
        screen.blit(Background, (0,0))
        font = pygame.font.SysFont("",100)
        graphics = font.render("Left Side Wins!",1,LBLUE)
        gameWindow.blit(graphics,(100,200))
        font = pygame.font.SysFont("",50)
        graphics = font.render("Window will automaticly close",1,LBLUE)
        gameWindow.blit(graphics,(100,325))
        pygame.display.update()
        print "Final Score. Left Team:",scoreL, "Right Team:",scoreR
        print "Time Elapsed = ",round(float(elapsed)/1000,2),"Seconds"

def endScreenTwo(scoreL,scoreR):
        screen.blit(Background, (0,0))
        font = pygame.font.SysFont("",100)
        graphics = font.render("Right Side Wins!",1,LBLUE)
        gameWindow.blit(graphics,(100,200))
        font = pygame.font.SysFont("",50)
        graphics = font.render("Window will automaticly close",1,LBLUE)
        gameWindow.blit(graphics,(100,325))
        pygame.display.update()
        print "Final Score. Left Team:",scoreL, "Right Team:",scoreR
        print "Time Elapsed = ",round(float(elapsed)/1000,2),"Seconds"

BEGIN = pygame.time.get_ticks()
#---------------------------#
# Main program begins here  #
#---------------------------#
usedL = 1
usedR = 1
print "Hit ESC to end the program."
inPlay = True
while inPlay == True:
    elapsed = pygame.time.get_ticks() - BEGIN
    redrawgameWindow(scoreL,scoreR)
    pygame.time.delay(2)

#Checks for presseed keys
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_UP]:
        if paddleRY == 0:
            paddleRY = paddleRY
        else:
            paddleRY = paddleRY - paddleRShift
    if keys[pygame.K_DOWN]:
        paddleRY = paddleRY + paddleRShift
    if keys[pygame.K_w]:
        paddleLY = paddleLY - paddleLShift
    if keys[pygame.K_s]:
        paddleLY = paddleLY + paddleLShift

        # bounce the ball from the paddle
    if paddleRH == 180:
        if ballX >= paddleRX and ballX <= paddleRX+paddleRW and ballY+ballR >= paddleRY and ballY+ballR <= paddleRY+180:
            speedX = -speedX
    if paddleLH == 180:
        if ballX >= paddleLX and ballX <= paddleLX+paddleLW and ballY+ballR >= paddleLY and ballY+ballR <= paddleLY+180:
            speedX = -speedX
    if ballX >= paddleRX and ballX <= paddleRX+paddleRW and ballY+ballR >= paddleRY-5 and ballY+ballR <= paddleRY+125:
        speedX = -speedX
    if ballX >= paddleLX and ballX <= paddleLX+paddleLW and ballY+ballR >= paddleLY-5 and ballY+ballR <= paddleLY+125:
        speedX = -speedX
# Stops Paddle from going off the screen
    if paddleRY<0:
        paddleRY = 0
    if paddleRY>480:
        paddleRY = 480
    if paddleLY<0:
        paddleLY = 0
    if paddleLY>480:
        paddleLY = 480    

# bounce the Top and Bottom Borders
    if ballX <= LEFT:
        ballR = 15
        ballX = WIDTH/2
        ballY =2*ballR
        speed = randint(0,1)
        scoreR = scoreR + 1
        if speed == 0:
            speedX = 5
            speedY = 5
        else:
            speedX = -5
            speedY = 5
    if ballX >= RIGHT:
        ballR = 15
        ballX = WIDTH/2
        ballY =2*ballR
        speed = randint(0,1)
        scoreL = scoreL + 1
        if speed == 0:
            speedX = 5
            speedY = 5
        else:
            speedX = -5
            speedY = 5
    if ballY<=TOP:
        speedY = -speedY
    if ballY>=HEIGHT-15:
        speedY = -speedY

# Cheat
    if usedL == 1:
        if keys[pygame.K_p]:
            speedX = -5
            usedL = 0
    if usedR == 1:
        if keys[pygame.K_z]:
            speedX = 5
            usedR = 0

# move the ball
    ballX = ballX + speedX
    ballY = ballY + speedY

# Increase speed
    if elapsed > 60000 and speedX == 5:
            speedX = 6
    if elapsed > 60000 and speedY == 5:
            speedY = 6
    if elapsed > 60000 and speedX == -5:
            speedX = -6
    if elapsed > 60000 and speedY == -5:
            speedY = -6
        
# End Screen
    if scoreL == 7:
        endScreenOne(scoreL,scoreR)
        pygame.time.delay(5000)
        inPlay = False
    if scoreR == 7:
        endScreenTwo(scoreL,scoreR)
        pygame.time.delay(5000)
        inPlay = False
#---------------------------------------# 
pygame.quit()
    

