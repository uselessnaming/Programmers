# 공원 산책
# 2024.06.21
# Lv1
def solution(park, routes):
    start_x, start_y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start_x, start_y = i, j
                break

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for route in routes:
        print(start_x, start_y)
        way, dist = route.split()
        dist = int(dist)

        idx = -1
        if way == "E":
            idx = 0
        elif way == "S":
            idx = 1
        elif way == "N":
            idx = 3
        elif way == "W":
            idx = 2

        isPossible = True

        xx, yy = start_x, start_y
        for i in range(dist):
            xx += dx[idx]
            yy += dy[idx]
            if not (0 <= xx < len(park) and 0 <= yy < len(park[0])) or park[xx][yy] == "X":
                isPossible = False
                break

        if isPossible:
            start_x += dx[idx] * dist
            start_y += dy[idx] * dist

    answer = [start_x, start_y]
    return answer

park1 = ["SOO","OOO","OOO"]
routes1 = ["E 2","S 2","W 1"]
# result [2, 1]

park2 = ["SOO","OXX","OOO"]
routes2 = ["E 2","S 2","W 1"]
# result [0, 1]

park3 = ["OSO","OOO","OXO","OOO"]
routes3 = ["E 2","S 3","W 1"]
# result [0, 0]

print(solution(park1, routes1))