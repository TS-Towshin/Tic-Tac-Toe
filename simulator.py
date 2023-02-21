import random
import time

def tic_tac_tow(position_list):

    board = ['1', '2', '3',
            '4', '5', '6',
            '7', '8', '9']
    i = 0
    try:
        while i <= 9:
            print()
            if i%2 == 0:
                pos = random.choice(position_list)
                position_list.remove(pos)
                charecter = 'X'
            elif i%2 == 1:
                pos = random.choice(position_list)
                position_list.remove(pos)
                charecter = 'O'
            i += 1
            if board[pos-1].isdigit():
                board[pos-1] = charecter
            else:
                print('This cell is occupied')
                i -= 1
            x_win = ['X', 'X', 'X']
            o_win = ['O', 'O', 'O']
            if board[0:3] == x_win:
                return 'X'
                
            elif board[0:3] == o_win:
                return 'O'
                
            elif board[3:6] == x_win:
                return 'X'
                
            elif board[3:6] == o_win:
                return 'O'
                
            elif board[6:9] == x_win:
                return 'X'
                
            elif board[6:9] == o_win:
                return 'O'
                
            elif board[0::3] == x_win:
                return 'X'
                
            elif board[0::3] == o_win:
                return 'O'
                
            elif board[1::3] == x_win:
                return 'X'
                
            elif board[1::3] == o_win:
                return 'O'
                
            elif board[2::3] == x_win:
                return 'X'
                
            elif board[2::3] == o_win:
                return 'O'
                
            elif board[0::4] == x_win:
                return 'X'
                
            elif board[0::4] == o_win:
                return 'O'
                
            elif board[2:7:2] == x_win:
                return 'X'
                
            elif board[2:7:2] == o_win:
                return 'O'
    except:
        return 'draw'

start = time.time()
x = 0
o = 0
draw = 0
cycle = 1000
for i in range(cycle):
    position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = tic_tac_tow(position_list)
    if result == 'X':
        x += 1
    elif result == 'O':
        o += 1
    elif result == 'draw':
        draw += 1
end = time.time()
time_taken = end-start
print(f"Time taken: {time_taken}s")
print(f"X = {x}\nO = {o}\nDraw = {draw}")
print(f"X won {(x/(x+o+draw))*100}% of the time")
print(f"O won {(o/(x+o+draw))*100}% of the time")
print(f"It was draw {(draw/(x+o+draw))*100}% of the time")
