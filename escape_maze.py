# 미로 탈출
# 2024.06.28
# Lv2
from collections import deque
def solution(maps):

    def bfs(start_x, start_y, start_n, target):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
        visited[start_x][start_y] = start_n

        q = deque([(start_x, start_y)])
        while q:
            print(q)
            x, y = q.popleft()
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < len(maps) and 0 <= yy < len(maps[0]):
                    if not visited[xx][yy] and maps[xx][yy] == target:
                        return visited[x][y] + 1
                    elif not visited[xx][yy] and maps[xx][yy] != "X":
                        visited[xx][yy] = visited[x][y] + 1
                        q.append((xx, yy))
        return -1

    start_x, start_y = 0, 0
    lever_x, lever_y = 0, 0

    # 시작 위치 탐색
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start_x, start_y = i, j
            elif maps[i][j] == "L":
                lever_x, lever_y = i, j

    result_l = bfs(start_x, start_y, 0, "L")
    if result_l == -1:
        return -1
    result_e = bfs(lever_x, lever_y, result_l, "E")
    if result_e == -1:
        return -1
    return result_e
map1 = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# result 16
map2 = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
# result -1
map3 = ["SELXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"]
# result 3
print(solution(map2))