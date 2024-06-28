# 혼자서 하는 틱택토
# 2024.06.27
# Lv2
def solution(board):
    answer = 1

    o = 0
    x = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                o+=1
            elif board[i][j] == "X":
                x+=1

    # O보다 X가 많은 경우 -1
    if o < x:
        return 0
    # O와 X의 개수 차이가 1 이상인 경우 -1
    elif abs(o-x) > 1:
        return 0

    # O가 먼저 3개 연결된 경우 O와 X의 개수가 같음 -1
    if o >= 3:
        success = False
        for i in range(3):
            if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
                success = True
            elif board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
                success = True
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            success = True
        elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
            success = True
        if success:
            if o == x:
                return 0

    # X가 먼저 3개를 연결한 경우 O가 X보다 많으면 -1
    if x >= 3:
        success = False
        for i in range(3):
            if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
                success = True
            elif board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
                success = True
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            success = True
        elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
            success = True
        if success:
            if o > x:
                return 0

    return answer

board1 = ["O.X", ".O.", "..X"] # result 1
board2 = ["OOO", "...", "XXX"] # result 0
board3 = ["...", ".X.", "..."] # result 0
board4 = ["...", "...", "..."] # result 1
print(solution(board4))