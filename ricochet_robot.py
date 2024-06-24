# 리코쳇 로봇
# 2024.06.24
# Lv2
from collections import deque
def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    start_x, start_y = 0, 0
    # 시작 지점 R을 찾아야 함
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                start_x, start_y = i, j

    visited[start_x][start_y] = 1
    # 4방향으로 갈 수 있는 곳까지 감
    # 이 때 visited를 체크하며 감
    # 마지막 위치가 G면 return cnt
    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()
        if board[x][y] == "G":
            return visited[x][y] - 1
        for i in range(4):
            xx, yy = x, y
            while True:
                xx += dx[i]
                yy += dy[i]
                if 0<=xx<len(board) and 0<=yy<len(board[0]) and board[xx][yy] == "D":
                    xx -= dx[i]
                    yy -= dy[i]
                    break
                if xx < 0 or xx >= len(board) or yy < 0 or yy >= len(board[0]):
                    xx -= dx[i]
                    yy -= dy[i]
                    break
            if not visited[xx][yy]:
                visited[xx][yy] = visited[x][y] + 1
                q.append((xx, yy))
    return -1

board1 = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
# result1 = 7
board2 = [".D.R", "....", ".G..", "...D"]
# result2 = -1

print(solution(board1))