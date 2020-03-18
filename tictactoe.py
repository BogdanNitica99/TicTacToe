from math import inf as infinity
from random import choice

board_web = [[None, None, None],
             [None, None, None],
             [None, None, None]]
# -------------------------------------------------------------Ai 3 MiniMa


def mini_max(state, depth, player, Comp):
    if player == Comp:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state, Comp):
        score = evaluate(state, Comp)
        return [-1, -1, score]

    for move in free_moves(state):
        x, y = move[0], move[1]
        state[x][y] = player
        score = mini_max(state, depth - 1, change_player(player), Comp)
        state[x][y] = None
        score[0], score[1] = x, y

        if player == Comp:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best


def ai_3(board, Ai):
    depth = len(free_moves(board))
    if depth == 0 or game_over(board, Ai):
        return
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = mini_max(board, depth, Ai, Ai)
        x, y = move[0], move[1]
    set_move(x, y, Ai)


def evaluate(state, Comp):
    if check_winner(state, Comp):
        score = +1
    elif check_winner(state, change_player(Comp)):
        score = -1
    else:
        score = 0

    return score


def free_moves(state):
    Moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] is None:
                Moves.append([i, j])
    return Moves


def game_over(state, Comp):
    return check_winner(state, Comp) or check_winner(
        state, change_player(Comp))


def change_player(player):
    if player == 'O':
        player = 'X'
    else:
        player = 'O'
    return player


def valid_move(x, y):
    if [x, y] in free_moves(grid):
        return True
    else:
        return False


def set_move(x, y, player):
    if valid_move(x, y):
        grid[x][y] = player
        return True
    else:
        return False

# -------------------------------------------------------------------------------------------------------------


def check_winner(state, player):
    stri = str(player + player + player)

    for i in range(3):
        check1 = ''
        check2 = ''
        check3 = ''
        check4 = ''
        for j in range(3):
            check1 += str(state[i][j])
            check2 += str(state[j][i])
            check3 += str(state[j][j])
            check4 += str(state[j][2 - j])
        if check1 == stri or check2 == stri or check3 == stri or check4 == stri:
            return True
    return False


def transforming_values(value):
    pos_x, pos_y = -1, -1

    if value == 0:
        pos_x, pos_y = 0, 0
    if value == 1:
        pos_x, pos_y = 0, 1
    if value == 2:
        pos_x, pos_y = 0, 2

    if value == 3:
        pos_x, pos_y = 1, 0
    if value == 4:
        pos_x, pos_y = 1, 1
    if value == 5:
        pos_x, pos_y = 1, 2

    if value == 6:
        pos_x, pos_y = 2, 0
    if value == 7:
        pos_x, pos_y = 2, 1
    if value == 8:
        pos_x, pos_y = 2, 2

    return (pos_x, pos_y)


def reset_game():
    global board_web

    board_web = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]


def game_mode_web1(value, playerWeb):
    global board_web

    (pos_x, pos_y) = transforming_values(int(value))

    board_web[pos_x][pos_y] = playerWeb

    is_game_over = game_over(board_web, 'X')

    if is_game_over == True or len(free_moves(board_web)) == 0:
        winner = 'Draw'
        if check_winner(board_web, 'X') == True:
            winner = 'X'
        elif check_winner(board_web, 'O') == True:
            winner = 'O'
        return (is_game_over, winner)
    else:
        return (False, -1)


def game_mode_web2(value, playerWeb):
    # Need to make this function
    return (True, 0)
