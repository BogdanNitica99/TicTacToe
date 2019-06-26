from math import inf as infinity
from random import choice
import pygame
from pygame.locals import *

import Graphics as G

pygame.init()

imgX = pygame.image.load('x.png')
imgX = pygame.transform.scale(imgX,(100,100))

imgY = pygame.image.load('O.png')
imgY = pygame.transform.scale(imgY,(100,100))

grid = [ [ None, None, None ], \
         [ None, None, None ], \
         [ None, None, None ] ]

def DrawBoard(Windows):
    pygame.draw.line(Windows, (255,255,255), (100,0), (100,300),2)
    pygame.draw.line(Windows, (255,255,255), (200,0), (200,300),2)

    pygame.draw.line(Windows, (255,255,255), (0,100), (300,100),2)
    pygame.draw.line(Windows, (255,255,255), (0,200), (300,200),2)

    for i in range (3):
        for j in range(3):
            if grid[i][j] == 'X':
                Windows.blit(imgX, (j*100, i*100))
            elif grid[i][j] == 'O':
                Windows.blit(imgY, (j*100, i*100))

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

def clickBoard():
    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = BoardPos(mouseX, mouseY)

    if(row >= 0 and col >= 0):
        if(grid[row][col] == None):
            return (row, col)    
    return (-1,-1)

#-------------------------------------------------------------Ai 3 MiniMax Alg -------------------------------

def miniMax(state, depth, player, Comp):
    if player == Comp:
        best = [-1,-1,-infinity]
    else:
        best = [-1,-1,+infinity]
    
    if depth == 0 or gameOver(state, Comp):
        score = evaluate(state, Comp)
        return [-1, -1, score]

    for move in freeMoves(state):
        x, y = move[0], move[1]
        state[x][y] = player
        score = miniMax(state, depth-1, changePlayer(player), Comp)
        state[x][y] = None
        score[0], score[1] = x,y

        if player == Comp:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
        
    return best
    
def AI3(board, Ai):
    depth = len(freeMoves(board))
    if depth == 0 or gameOver(board, Ai):
        return
    if depth == 9:
        x = choice([0,1,2])
        y = choice([0,1,2])
    else:
        move = miniMax(board, depth, Ai, Ai)
        x, y = move[0], move[1]
    set_move(x,y,Ai)

def evaluate(state, Comp):
    if CheckWinner(state, Comp):
        score = +1
    elif CheckWinner(state, changePlayer(Comp)):
        score = -1
    else:
        score = 0

    return score

def freeMoves(state):
    Moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == None:
                Moves.append([i,j])
    return Moves

def gameOver(state, Comp):
    return CheckWinner(state, Comp) or CheckWinner(state, changePlayer(Comp))

def changePlayer(player):
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    return player

def valid_move(x, y):
    if [x, y] in freeMoves(grid):
        return True
    else:
        return False

def set_move(x, y, player):
    if valid_move(x, y):
        grid[x][y] = player
        return True
    else:
        return False

#-------------------------------------------------------------------------------------------------------------

def CheckWinner(state, player):
    stri = str(player+player+player)
    #print(stri)
    for i in range (3):
        check1 = ''
        check2 = ''
        check3 = ''
        check4 = ''
        for j in range (3):
            check1 += str(state[i][j])
            check2 += str(state[j][i])
            check3 += str(state[j][j])
            check4 += str(state[j][2-j])
        if check1 == stri or check2 == stri or check3 == stri or check4 == stri:
            return True
    return False

def GameMode1(Windows):
    winner = None
    isGameOver = False
    player = 1

    G.ShowStatus(Windows,'Player1', 'Player2', player)
    G.BackToMenu(Windows)
    
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type is MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if mouseX >=350 and mouseX <= 500 and mouseY >= 100 and mouseY <= 170:
                    run = False
                if isGameOver == False and len(freeMoves(grid)) != 0:
                    (x,y) = clickBoard()
                    if (x,y) != (-1,-1):
                        if player == 1:
                            grid[x][y] = 'X'
                            player = 2
                        else:
                            grid[x][y] = 'O'
                            player = 1
            if isGameOver == True or len(freeMoves(grid)) == 0:
                winner = 'Draw'
                if CheckWinner(grid, 'X') == True:
                    winner = 'X'
                elif CheckWinner(grid, 'O') == True:
                    winner = 'O'
            isGameOver = gameOver(grid, 'X')
            Windows.fill((0,0,0))
            DrawBoard(Windows)
            G.BackToMenu(Windows)
            G.ShowStatus(Windows,'Player1', 'Player2', player)
            G.ShowWinner(Windows, winner)
    return -1

def GameMode2(Windows):
    isGameOver = False
    winner = None
    turn = 1
    tturn = 1

    Pl, AI, turn = G.SettingTheGame(Windows)
    
    Windows.fill((0,0,0))
    
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if isGameOver == False and len(freeMoves(grid)) != 0:
                if turn == 1:
                    if event.type is MOUSEBUTTONDOWN:
                        (x,y) = clickBoard()
                        if(x,y) != (-1,-1):
                            grid[x][y] = Pl
                            turn = 2
                            tturn=-tturn
                else:
                    AI3(grid, AI)
                    turn = 1
                    tturn = -tturn
            if isGameOver == True or len(freeMoves(grid)) == 0:
                winner = 'Draw'
                if CheckWinner(grid, AI) == True:
                    winner = AI
                elif CheckWinner(grid, Pl) == True:
                    winner = Pl
            Windows.fill((0,0,0))
            G.ShowWinner(Windows, winner)
            DrawBoard(Windows)
            if AI == 'X':
            	G.ShowStatus(Windows, 'Robot ','Player ', tturn)
            else:
            	G.ShowStatus(Windows, 'Player ','Robot ', tturn)
            isGameOver = gameOver(grid, AI)
    return 1

def ResetMap():
	for i in range(3):
		for j in range(3):
			grid[i][j] = None

def main():
    mode = -1
    Windows = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Tic-Tac-Toe')
    
    while mode == -1:
        Windows.fill((0,0,0))    

        ResetMap()

        gameMode = G.gameIntro(Windows)

        Windows.fill((0,0,0))

        if gameMode == 1:
            mode = GameMode1(Windows)
        else:
            mode = GameMode2(Windows)
        
    pygame.quit()

main()
    
