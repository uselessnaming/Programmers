# 당구연습
# 2024.06.25
# Lv2
# 해답 참고 : 수학적 사고 (대칭 이동)
def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        print(ball)
        x, y = ball[0], ball[1]
        if x == startX:
            if y > startY:
                answer.append(min((startY + y) ** 2, (y - startY) ** 2 + 4 * min(x, m - x) ** 2))
            else:
                answer.append(min((2 * n - startY - y) ** 2, (y - startY) ** 2 + 4 * min(x, m - x) ** 2))
        elif y == startY:
            if x > startX:
                answer.append(min((startX + x) ** 2, (x - startX) ** 2 + 4 * min(y, n - y) ** 2))
            else:
                answer.append(min((2 * m - startX - x) ** 2, (x - startX) ** 2 + 4 * min(y, n - y) ** 2))
        else:
            answer.append(min((x - startX) ** 2 + min(startY + y, 2 * n - startY - y) ** 2, (y - startY) ** 2 + min(startX + x, 2 * m - startX - x) ** 2))
    return answer

m = 10
n = 10
startX = 3
startY = 7
balls = [[7,7],[2,7],[7,3]]

print(solution(m,n,startX,startY,balls))