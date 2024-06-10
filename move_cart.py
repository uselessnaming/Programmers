# 수레 움직이기
# 2024.06.10
# 참고.. 해서 풀었담..
from collections import deque
import copy
def solution(maze):
    # 1 >> 빨수레 시작 / 2 >> 빨 수레 도착 
    # 3 >> 파 수레 시작 / 4 >> 파 수레 도착
    # 5 >> 벽
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    r_start_x, r_start_y = 0, 0
    b_start_x, b_start_y = 0, 0

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                r_start_x, r_start_y = i, j
            elif maze[i][j] == 2:
                b_start_x, b_start_y = i, j
            elif maze[i][j] == 5:
                visited[i][j] = True

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    red_arrive, blue_arrive = False, False

    q = deque([(r_start_x, r_start_y, b_start_x, b_start_y, 0, visited, visited)])

    while q:
        rx, ry, bx, by, cnt, vr_tmp, vb_tmp = q.popleft()

        r_visited = copy.deepcopy(vr_tmp)
        b_visited = copy.deepcopy(vb_tmp)
        r_visited[rx][ry] = True
        b_visited[bx][by] = True

        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            return cnt
        else:
            if maze[rx][ry] == 3:
                red_arrive = True
                blue_arrive = False
            elif maze[bx][by] == 4:
                red_arrive = False
                blue_arrive = True
            else:
                red_arrive = False
                blue_arrive = False

        for i in range(4):
            if red_arrive:
                bxx = bx + dx[i]
                byy = by + dy[i]

                if is_bounded(bxx, byy, len(maze), len(maze[0])):
                    if not ((b_visited[bxx][byy]) or (is_overlapper(rx, ry, bxx, byy))):
                        q.append((rx, ry, bxx, byy, cnt + 1, r_visited, b_visited))

            elif blue_arrive:
                rxx = rx + dx[i]
                ryy = ry + dy[i]

                if is_bounded(rxx, ryy, len(maze), len(maze[0])):
                    if not ((r_visited[rxx][ryy]) or (is_overlapper(rxx, ryy, bx, by))):
                        q.append((rxx, ryy, bx, by, cnt + 1, r_visited, b_visited))
            else:
                rxx = rx + dx[i]
                ryy = ry + dy[i]
                if is_bounded(rxx, ryy, len(maze), len(maze[0])):
                    if not r_visited[rxx][ryy]:
                        for j in range(4):
                            bxx = bx + dx[j]
                            byy = by + dy[j]

                            if is_bounded(bxx, byy, len(maze), len(maze[0])):
                                if not ((b_visited[bxx][byy]) or (is_switched(rx, ry, bx, by, rxx, ryy, bxx, byy)) or (is_overlapper(rxx, ryy, bxx, byy))):
                                    q.append((rxx, ryy, bxx, byy, cnt + 1, r_visited, b_visited))
    return 0

def is_bounded(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

def is_overlapper(rx, ry, bx, by):
    return (rx, ry) == (bx, by)

def is_switched(rx, ry, bx, by, rxx, ryy, bxx, byy):
    return (rxx, ryy) == (bx, by) and (bxx, byy) == (rx, ry)

maze1 = [[1, 4], [0, 0], [2, 3]] #result 3
maze2 = [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]] #result 7
maze3 = [[1, 5], [2, 5], [4, 5], [3, 5]] #result 0
maze4 = [[4,1,2,3]] #result 0

print(solution(maze4))