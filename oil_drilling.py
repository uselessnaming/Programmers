# 석유 시추
# 2024.06.08
# Try 2 : Failed 1 + Success 1
from collections import deque
import copy
def solution(land):
    answer = 0

    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    values = {}

    def bfs(current_x, current_y, idx):
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

        q = deque([(current_x, current_y)])
        cnt = 0
        while q:
            x, y = q.popleft()
            x, y = int(x), int(y)

            if visited[x][y]:
                continue

            visited[x][y] = True
            land[x][y] = idx
            cnt += 1

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]

                if 0 <= xx < len(land) and 0 <= yy < len(land[0]):
                    if not visited[xx][yy] and land[xx][yy] == 1:
                        q.append((xx, yy))
        return cnt

    # 전체 land 에 대한 bfs를 통해서 각 땅의 크기를 번호와 함께 마킹
    idx = 1
    for i in range(len(land)):
        for j in range(len(land[0])):
            if not visited[i][j] and land[i][j] == 1:
                values[idx] = bfs(i, j, idx)
                idx += 1

    # land[0][0] ~ land[0][n] 까지 돌면서 마킹된 숫자에 따라 값을 더해서 확인
    for j in range(len(land[0])):
        markers = set()
        for i in range(len(land)):
            if land[i][j] != 0:
                markers.add(land[i][j])
        s = 0

        for marker in markers:
            s += values[marker]

        if s > answer:
            answer = s

    return answer

## 실패 case 1
## 시간 초과
def failed_solution(land):
    def bfs(current_x, current_y, land_copy):
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

        q = deque([(current_x, current_y)])
        cnt = 0
        while q:
            x, y = q.popleft()
            x, y = int(x), int(y)

            if land_copy[x][y] == 1:
                land_copy[x][y] = -1
                cnt += 1

                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]

                    if 0 <= xx < len(land_copy) and 0 <= yy < len(land_copy[0]):
                        if land_copy[xx][yy] == 1:
                            q.append((xx, yy))
        return cnt

    # 0 ~ 최대 길이까지 전체를 돌며 해당 라인에 있는 석유의 크기를 확인
    for i in range(len(land[0])):
        tmp = copy.deepcopy(land)
        total = 0
        for j in range(len(land)):
            total += bfs(j, i, tmp)

        if total > answer:
            answer = total

    return answer

land1 = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
land2 = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(land2))