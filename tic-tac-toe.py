import random
import pygame
from pygame.locals import *
pygame.init()

status = 'X'
grid = [ [ None, None, None ], \
         [ None, None, None ], \
         [ None, None, None ] ]

priorityGrid = [ [ 0, 0, 0], \
                 [ 0, 0, 0], \
                 [ 0, 0, 0] ]

def DrawBoard(Windows):

    imgX = pygame.image.load('x.png')
    imgX = pygame.transform.scale(imgX,(100,100))
    #imgY = pygame.image.load('y.bmp')

    

    pygame.draw.line(Windows, (255,255,255), (100,0), (100,300),2)
    pygame.draw.line(Windows, (255,255,255), (200,0), (200,300),2)

    pygame.draw.line(Windows, (255,255,255), (0,100), (300,100),2)
    pygame.draw.line(Windows, (255,255,255), (0,200), (300,200),2)

    for i in range (3):
        for j in range(3):
            if grid[i][j] == 'X':
                #DrawXand0(Windows, i, j, 1)
                Windows.blit(imgX, (j*100, i*100))
            elif grid[i][j] == 'O':
                DrawXand0(Windows, i, j, 2)

    pygame.display.update()

    
def BoardPos(mouseX, mouseY):
    if(mouseY < 100):
        row = 0
    elif(mouseY < 200):
        row = 1
    elif(mouseY < 300):
        row = 2
    else:
        row = -1

    if(mouseX < 100):
        col = 0
    elif(mouseX < 200):
        col = 1
    elif(mouseX < 300):
        col = 2
    else:
        col = -1

    return (row, col)


def ShowStatus(Windows, player, winner):    #Afisez info. utile jocului such as Al cui rand este sa mute, ce culoare are fiecare jucator
    font = pygame.font.SysFont('comicsans', 27, True)
    
    textPlayer1 = font.render('Player 1: X', 1, (255,0,0))
    Windows.blit(textPlayer1, (360,10))
    textPlayer2 = font.render('Player 2: O', 1, (255,0,0))
    Windows.blit(textPlayer2, (360,25))
    
    textTurn = font.render('Is Turn for :', 1, (255,255,255))
    Windows.blit(textTurn, (360, 40))
    if player == 1:
        textTurnPlayer = font.render(' X', 1, (255,255,255))
        Windows.blit(textTurnPlayer, (468, 40))
    else:
        textTurnPlayer = font.render(' O', 1, (255,255,255))
        Windows.blit(textTurnPlayer, (468, 40))
        
    if winner == 1:
        textWinner1 = font.render('Player 1 WON', 1, (255,255,0))
        Windows.blit(textWinner1, (10,460))
    elif winner == 2:
        textWinner2 = font.render('Player 2 WON', 1, (255,255,0))
        Windows.blit(textWinner2, (10,460))
    pygame.display.update()

def clickBoard(board, player):
    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = BoardPos(mouseX, mouseY)

    if(row >= 0 and col >= 0):
        if(grid[row][col] == None):
            if player == 1:
                grid[row][col] = 'X'
            else:
                grid[row][col] = 'O'

            return 1    #returnez 1 daca am reusit sa dau click (clickul este valabil)
    return 0    #returnez 0 daca clickul nu a fost ok

def DrawXand0(board, bRow, bCol, stats):
    centerX = ((bCol) * 100) + 50
    centerY = ((bRow) * 100) + 50

    if (stats == 2):
        pygame.draw.circle (board, (255,255,255), (centerX, centerY), 44, 2)
    else:
        pygame.draw.line (board, (255,255,255), (centerX - 22, centerY - 22), \
                         (centerX + 22, centerY + 22), 2)
        pygame.draw.line (board, (255,255,255), (centerX + 22, centerY - 22), \
                         (centerX - 22, centerY + 22), 2)

def CheckWinner():
    for i in range (3):
        check1 = ''
        check2 = ''
        check3 = ''
        check4 = ''
        for j in range (3):
            check1 += str(grid[i][j])
            check2 += str(grid[j][i])
            check3 += str(grid[j][j])
            check4 += str(grid[j][2-j])
        if check1 == 'XXX' or check2 == 'XXX' or check3 == 'XXX' or check4 == 'XXX':
            return 1
        if check1 == 'OOO' or check2 == 'OOO' or check3 == 'OOO' or check4 == 'OOO':
            return 2
    return 0


def gameIntro(Windows):     #Primul ecran, cu cele doua butoane in care selectez gameModul si dau informatii despre joc
    intro = True

    font1 = pygame.font.SysFont('comicsans', 70, True)
    font2 = pygame.font.SysFont('comicsans', 25, True)
    
    textNameGame = font1.render('Tic-Tac-Toe', 1, (255,0,255))
    Windows.blit(textNameGame, (100,10))

    pygame.draw.rect(Windows, (255,0,0), (70, 100, 150,90), 0)
    textButton1 = font2.render('Human v Human', 1, (0,255,255))
    Windows.blit(textButton1, (73,135))

    pygame.draw.rect(Windows, (255,0,0), (270, 100, 150,90), 0)
    textButton2 = font2.render('Human v AI', 1, (0,255,255))
    Windows.blit(textButton2, (285,135))

    textInfo1 = font2.render('A game made by Nitica Bogdan for fun', 1, (0,255,255))
    Windows.blit(textInfo1, (10,300))

    textInfo2 = font2.render('Built 0.1', 1, (0,255,255))
    Windows.blit(textInfo2, (10,350))
    
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

def GameMode1(Windows):
    winner = 0
    player = 1

    ShowStatus(Windows, player, winner)
    
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type is MOUSEBUTTONDOWN:
                if winner == 0:
                    clickOk = clickBoard(Windows, player)
                    if clickOk == 1:
                        if player == 1:
                            player = 2
                        else:
                            player = 1
                        winner = CheckWinner()
            Windows.fill((0,0,0))
            DrawBoard(Windows)
            ShowStatus(Windows, player, winner)
    return False

def AI1():
    ok = True

    while ok:
    
        x = random.randint(0,3) - 1
        y = random.randint(0,3) - 1

        if(grid[x][y] == None):
            grid[x][y] = 'O'
            ok = False


def ChooseWhoToPlay(Windows):
    intro = True

    font1 = pygame.font.SysFont('comicsans', 50, True)
    font2 = pygame.font.SysFont('comicsans', 40, True)
    
    textName = font1.render('Choose who to Play', 1, (255,0,255))
    Windows.blit(textName, (100,10))

    pygame.draw.rect(Windows, (255,0,0), (70, 100, 60,60), 0)
    textButton1 = font2.render('X', 1, (0,255,255))
    Windows.blit(textButton1, (90,120))

    pygame.draw.rect(Windows, (255,0,0), (150, 100, 150,60), 0)
    textButton2 = font2.render('Random', 1, (0,255,255))
    Windows.blit(textButton2, (160,120))

    pygame.draw.rect(Windows, (255,0,0), (320, 100, 60,60), 0)
    textButton3 = font2.render('O', 1, (0,255,255))
    Windows.blit(textButton3, (340,120))
    
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

def GameMode2(Windows):
    winner = 0
    player = 1

    Pl = ChooseWhoToPlay(Windows)
    print(Pl)

    Windows.fill((0,0,0))

    ShowStatus(Windows, player, winner)

    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif player == 1 and winner == 0:
                if event.type is MOUSEBUTTONDOWN:
                    clickOk = clickBoard(Windows, player)
                    if clickOk == 1:
                        player = 2
            elif player == 2 and winner == 0:
                AI1()

                player = 1
            winner = CheckWinner()
            Windows.fill((0,0,0))
            DrawBoard(Windows)
            ShowStatus(Windows, player, winner)
    return False

def main():
    Windows = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Tic-Tac-Toe')

    gameMode = gameIntro(Windows)

    Windows.fill((0,0,0))

    if gameMode == 1:
        GameMode1(Windows)
    else:
        GameMode2(Windows)
        
    pygame.quit()

main()
    
