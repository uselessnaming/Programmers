# 두 원 사이의 정수 쌍
# 2024.06.14
# Lv2
# 1차 시간 초과 (7~10 case)
# 2차 시간 초과 (7~10 case)
# 3차 시간 초과 (7~10 case)
# 결과적으로 원의 방정식을 이용해 해결하지 않으면 시간 초과로 해결할 수 없음 
import math
def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        maxY = math.sqrt(r2*r2 - i*i)
        minY = 0 if r1 <= i else math.sqrt(r1*r1 - i*i)
        answer += math.floor(maxY) - math.ceil(minY) + 1
        
    return answer * 4

print(solution(10, 20))
#2 4 40
#9 20 1008
#10 20 952
#999999 1000000 6281440

def failed_solution(r1, r2):
    # 4분면이니 1분면 중 반만 가지고 내부 점을 테스트 한 후 *8
    # x, y 선에 있는 점들 계산
    # + (r * 4 + 1)
    r2_dots = 0
    r1_dots = 0
    for i in range(1, r2 + 1):
        for j in range(1, r2 + 1):
            if j > i:
                if r2 * r2 >= j * j + i * i:
                    r2_dots += 1
    r2_dots *= 2
    for i in range(r2, 0, -1):
        if r2 * r2 >= i * i * 2:
            max_diagonal = i
            break
    r2_dots += max_diagonal + r2

    for i in range(1, r1 + 1):
        for j in range(1, r1 + 1):
            if j > i:
                if r1 * r1 > j * j + i * i:
                    r1_dots += 1
    r1_dots *= 2
    for i in range(r1, 0, -1):
        if r1 * r1 > i * i * 2:
            max_diagonal = i
            break
    r1_dots += max_diagonal + r1 - 1

    answer = (r2_dots - r1_dots) * 4
    return answer

def failed_solution2(r1, r2):
    # 4분면이니 1분면 중 반만 가지고 내부 점을 테스트 한 후 *8
    # x, y 선에 있는 점들 계산
    # + (r * 4 + 1)
    dots = 0
    for i in range(1, r2 + 1):
        for j in range(1, r2 + 1):
            if j > i:
                if r2 * r2 >= j * j + i * i and r1 * r1 < j * j + i * i:
                    dots += 1

    for i in range(r2, 0, -1):
        if r2 * r2 >= i * i * 2:
            max_diagonal = i
            break
    dots = (dots * 2) + max_diagonal + (r2 - r1)

    answer = dots * 4
    return answer

def failed_solution3(r1,r2):
    # 4분면이니 1분면 중 반만 가지고 내부 점을 테스트 한 후 *8
    # x, y 선에 있는 점들 계산
    dots = 0
    diagonal_dots = 0
    for i in range(1, r2 + 1):
        for j in range(i, r2 + 1):
            if j > i:
                if r1 * r1 <= j * j + i * i <= r2 * r2:
                    dots += 1
            if i == j:
                if r1 * r1 <= i * i * 2 <= r2 * r2:
                    diagonal_dots += 1
    print(dots, diagonal_dots)

    dots = (dots * 2) + diagonal_dots + (r2 - r1 + 1)
    print(dots)

    answer = dots * 4
    return answer
