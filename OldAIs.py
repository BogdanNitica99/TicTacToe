def AI1():
    ok = True

    while ok:
    
        x = random.randint(0,3) - 1
        y = random.randint(0,3) - 1

        if(grid[x][y] == None):
            ok = False

    return (x,y)

def CheckWinningOrLosing():#Choosing the best place for the AI to move
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

        if check1 == 'XXNone' or check1 == 'NoneXX' or check1 == 'XNoneX':
            if check1 == 'XXNone':
                return (i,j)
            if check1 == 'XNoneX':
                return (i,1)
            if check1 == 'NoneXX':
                return (i,0)
        if check2 == 'XXNone' or check2 == 'NoneXX' or check2 == 'XNoneX':
            if check2 == 'XXNone':
                return (2,i)
            if check2 == 'XNoneX':
                return (1,i)
            if check2 == 'NoneXX':
                return (0,i)
        if check3 == 'XXNone' or check3 == 'NoneXX' or check3 == 'XNoneX':
            if check3 == 'XXNone':
                return (2,2)
            if check3 == 'XNoneX':
                return (1,1)
            if check3 == 'NoneXX':
                return (0,0)
        if check4 == 'XXNone' or check4 == 'NoneXX' or check4 == 'XNoneX':
            if check4 == 'XXNone':
                return (2,0)
            if check4 == 'XNoneX':
                return (1,1)
            if check4 == 'NoneXX':
                return (0,2)

        if check1 == 'OONone' or check1 == 'NoneOO' or check1 == 'ONoneO':
            if check1 == 'OONone':
                return (i,j)
            if check1 == 'ONoneO':
                return (i,1)
            if check1 == 'NoneOO':
                return (i,0)
        if check2 == 'OONone' or check2 == 'NoneOO' or check2 == 'ONoneO':
            if check2 == 'OONone':
                return (2,i)
            if check2 == 'ONoneO':
                return (1,i)
            if check2 == 'NoneOO':
                return (0,i)
        if check3 == 'OONone' or check3 == 'NoneOO' or check3 == 'ONoneO':
            if check3 == 'OONone':
                return (2,2)
            if check3 == 'ONoneO':
                return (1,1)
            if check3 == 'NoneOO':
                return (0,0)
        if check4 == 'OONone' or check4 == 'NoneOO' or check4 == 'ONoneO':
            if check4 == 'OONone':
                return (2,0)
            if check4 == 'ONoneO':
                return (1,1)
            if check4 == 'NoneOO':
                return (0,2)

    return (-1,-1)

def AI2():
    ok = True

    while ok:
    
        x = random.randint(0,3) - 1
        y = random.randint(0,3) - 1

        (xaux, yaux) = CheckWinningOrLosing()
        if (xaux, yaux) != (-1, -1):
            (x,y) = (xaux, yaux)

        if(grid[x][y] == None):
            ok = False

    return (x,y)
