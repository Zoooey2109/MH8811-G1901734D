# Tic-Tac-Toe Drawing Module

def TicTacDraw(board):
    for i in range(len(board)):
        str = ""
        for j in range(len(board[i])):
            if board[i][j] == 0:
                str = str +" O |"
            elif board[i][j] == 1:
                str = str + " X |"
            elif board[i][j] == 2:
                str = str + "   |"
                if i != 0:
                    print(len(board)* "----")
        print(str[:-1])

TicTacDraw([[ 0, 1, 2 ], [ 2, 0, 0 ], [ 1, 1, 2 ]])
