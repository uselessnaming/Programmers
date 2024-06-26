# 바탕화면 정리
# 2024.06.26
# Lv1
def solution(wallpaper):
    min_x, min_y, max_x, max_y = len(wallpaper),len(wallpaper[0]),0,0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                if i < min_x:
                    min_x = i
                if j < min_y:
                    min_y = j
                if i > max_x:
                    max_x = i
                if j > max_y:
                    max_y = j
    answer = [min_x, min_y, max_x+1, max_y+1]
    return answer

wallpaper1 = [".#...", "..#..", "...#."]
# result [0,1,3,4]
wallpaper2 = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
# result [1,3,5,8]
wallpaper3 = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
# result [0,0,7,9]
wallpaper4 = ["..", "#."]
# result [1,0,2,1]
print(solution(wallpaper4))