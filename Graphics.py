import pygame
import random
from pygame.locals import *

def ShowStatus(Windows, name1, name2, player):
    font = pygame.font.SysFont('arial', 27, True)
    
    textPlayer1 = font.render(str(name1) + ': X', 1, (255,0,0))
    Windows.blit(textPlayer1, (360,10))
    textPlayer2 = font.render(str(name2) + ': O', 1, (255,0,0))
    Windows.blit(textPlayer2, (360,35))
    
    textTurn = font.render('Is Turn for :', 1, (255,255,255))
    Windows.blit(textTurn, (360, 60))
    if player == 1:
        textTurnPlayer = font.render(' X', 1, (255,255,255))
        Windows.blit(textTurnPlayer, (475, 60))
    else:
        textTurnPlayer = font.render(' O', 1, (255,255,255))
        Windows.blit(textTurnPlayer, (475, 60))
    pygame.display.update()

def ShowWinner(Windows, winner):
    font = pygame.font.SysFont('arial', 27, True)
    if winner != None:
        if winner == 'Draw':
            textWinner1 = font.render('Stalemate', 1, (255,255,0))
            Windows.blit(textWinner1, (10,460))
        else:
            textWinner3 = font.render(str(winner) + ' Won', 1, (255,255,0))
            Windows.blit(textWinner3, (10,460))
        #RestartLevel(Windows)
    pygame.display.update()

def BackToMenu(Windows):
    font2 = pygame.font.SysFont('arial', 25, True)

    pygame.draw.rect(Windows, (120,120,120), (350, 100, 150,70), 0)
    textButton1 = font2.render('Back to Menu', 1, (0,0,0))
    Windows.blit(textButton1, (360,115))

def gameIntro(Windows):
    intro = True

    font1 = pygame.font.SysFont('arial', 70, True)
    font2 = pygame.font.SysFont('arial', 25, True)
    
    textNameGame = font1.render('Tic-Tac-Toe', 1, (34,24,120))
    Windows.blit(textNameGame, (100,10))

    pygame.draw.rect(Windows, (255,0,0), (70, 100, 150,90), 0)
    textButton1 = font2.render('2 Players', 1, (0,255,255))
    Windows.blit(textButton1, (100,130))

    pygame.draw.rect(Windows, (255,0,0), (270, 100, 150,90), 0)
    textButton2 = font2.render('1 Player', 1, (0,255,255))
    Windows.blit(textButton2, (300,130))

    #textInfo1 = font2.render('A game made by Nitica Bogdan for fun', 1, (0,255,255))
    #Windows.blit(textInfo1, (10,300))

    #textInfo2 = font2.render('Version 0.2', 1, (0,255,255))
    #Windows.blit(textInfo2, (10,350))
    
    pygame.display.update()

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                quit()
            elif event.type is MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX >=70 and mouseX <= 220 and mouseY >= 100 and mouseY <= 190:
                    return 1
                elif mouseX >=270 and mouseX <= 420 and mouseY >= 100 and mouseY <= 190:
                    return 2

def ChooseWhoToPlay(Windows):
    intro = True

    font1 = pygame.font.SysFont('arial', 50, True)
    font2 = pygame.font.SysFont('arial', 40, True)
    
    textName = font1.render('Choose who to Play', 1, (37,122,31))
    Windows.blit(textName, (50,10))

    pygame.draw.rect(Windows, (130,130,130), (70, 100, 60,60), 0)
    textButton1 = font2.render('X', 1, (0,0,0))
    Windows.blit(textButton1, (87,105))

    pygame.draw.rect(Windows, (130,130,130), (150, 100, 150,60), 0)
    textButton2 = font2.render('Random', 1, (0,0,0))
    Windows.blit(textButton2, (160,105))

    pygame.draw.rect(Windows, (130,130,130), (320, 100, 60,60), 0)
    textButton3 = font2.render('O', 1, (0,0,0))
    Windows.blit(textButton3, (335,105))
    
    pygame.display.update()

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                quit()
            elif event.type is MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX >=70 and mouseX <= 130 and mouseY >= 100 and mouseY <= 160:
                    return 'X'
                elif mouseX >=150 and mouseX <= 300 and mouseY >= 100 and mouseY <= 160:
                    return 'R'
                elif mouseX >=320 and mouseX <= 380 and mouseY >= 100 and mouseY <= 160:
                    return 'O'

def SettingTheGame(Windows):
    turn = 0
    Pl = ChooseWhoToPlay(Windows)

    if Pl == 'R':
        a = random.randint(0,2)
        if a == 1:
            Pl = 'X'
        else:
            Pl = 'O'
    if Pl == 'O':
        AI = 'X'
        turn = 2
        ShowStatus(Windows, 'Robot ','Player ', turn)
    else:
        ShowStatus(Windows, 'Player ','Robot ', turn)
        AI = 'O'
        turn = 1
    return (Pl, AI, turn)
