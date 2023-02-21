def visualize(board):
    f1 = f'| {board[0]} | {board[1]} | {board[2]} |'
    f2 = f'| {board[3]} | {board[4]} | {board[5]} |'
    f3 = f'| {board[6]} | {board[7]} | {board[8]} |'
    lf1 = len(f1)
    lf2 = len(f2)
    print(f1)
    print('-'*lf1)
    print(f2)
    print('-'*lf2)
    print(f3)


board = ['1', '2', '3',
        '4', '5', '6',
        '7', '8', '9']
visualize(board)
i = 0
while i <= 9:
    try:
        print()
        if i%2 == 0:
            inp = int(input('X: '))
            charecter = 'X'
        elif i%2 == 1:
            inp = int(input('O: '))
            charecter = 'O'
        i += 1
        if board[inp-1].isdigit():
            board[inp-1] = charecter
        else:
            print('This cell is occupied')
            i -= 1
        visualize(board)
        x_win = ['X', 'X', 'X']
        o_win = ['O', 'O', 'O']
        if board[0:3] == x_win:
            print('X won')
            exit()
        elif board[0:3] == o_win:
            print('O won')
            exit()
        elif board[3:6] == x_win:
            print('X won')
            exit()
        elif board[3:6] == o_win:
            print('O won')
            exit()
        elif board[6:9] == x_win:
            print('X won')
            exit()
        elif board[6:9] == o_win:
            print('O won')
            exit()
        elif board[0::3] == x_win:
            print('X won')
            exit()
        elif board[0::3] == o_win:
            print('O won')
            exit()
        elif board[1::3] == x_win:
            print('X won')
            exit()
        elif board[1::3] == o_win:
            print('O won')
            exit()
        elif board[2::3] == x_win:
            print('X won')
            exit()
        elif board[2::3] == o_win:
            print('O won')
            exit()
        elif board[0::4] == x_win:
            print('X won')
            exit()
        elif board[0::4] == o_win:
            print('O won')
            exit()
        elif board[2:7:2] == x_win:
            print('X won')
            exit()
        elif board[2:7:2] == o_win:
            print('O won')
            exit()
    except Exception as why:
        print(why)
print('Its a draw')
