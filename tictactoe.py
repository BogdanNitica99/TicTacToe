from math import inf as infinity
from random import choice

boardWeb = [ [ None, None, None ], \
             [ None, None, None ], \
             [ None, None, None ] ]
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

def transformingValues(value):
    posX, posY = -1, -1

    if value == 0:
        posX, posY = 0, 0
    if value == 1:
        posX, posY = 0, 1
    if value == 2:
        posX, posY = 0, 2

    if value == 3:
        posX, posY = 1, 0
    if value == 4:
        posX, posY = 1, 1
    if value == 5:
        posX, posY = 1, 2

    if value == 6:
        posX, posY = 2, 0
    if value == 7:
        posX, posY = 2, 1
    if value == 8:
        posX, posY = 2, 2

    return (posX, posY)

def resetGame():
    global boardWeb

    boardWeb = [ [ None, None, None ], \
             [ None, None, None ], \
             [ None, None, None ] ]

def GameModeFromWeb1(value, playerWeb):
    global boardWeb

    (posX, posY) = transformingValues(int(value))

    boardWeb[posX][posY] = playerWeb

    isGameOver = gameOver(boardWeb, 'X')

    if isGameOver == True or len(freeMoves(boardWeb)) == 0:
        winner = 'Draw'
        if CheckWinner(boardWeb, 'X') == True:
            winner = 'X'
        elif CheckWinner(boardWeb, 'O') == True:
            winner = 'O'
        return (isGameOver, winner)
    else:
        return (False, -1)

    
