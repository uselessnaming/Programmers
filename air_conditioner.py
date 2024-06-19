# 에어컨
# 2024.06.19
# 정답 보고 풀었음
# DP 개념
# retry
def solution(temperature, t1, t2, a, b, onboard):
    t1 += 10
    t2 += 10
    temperature += 10

    dp = [[1000 * 100] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0

    flag = 1
    if temperature > t2:
        flag = -1

    for i in range(1, len(onboard)):
        for j in range(51):
            arr = [1000 * 100]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                if 0 <= j+flag <= 50:
                    arr.append(dp[i-1][j+flag])
                if j == temperature:
                    arr.append(dp[i-1][j])
                if 0 <= j-flag <= 50:
                    arr.append(dp[i-1][j-flag] + a)
                if t1 <= j <= t2:
                    arr.append(dp[i-1][j] + b)

                dp[i][j] = min(arr)

    return min(dp[len(onboard) - 1])

temperature1 = 28
t11 = 18
t21 = 26
a1, b1 = 10, 8
onboard1 = [0, 0, 1, 1, 1, 1, 1]
# result 40

temperature2 = -10
t12 = -5
t22 = 5
a2, b2 = 5, 1
onboard2 = [0, 0, 0, 0, 0, 1, 0]
# result 25

temperature3 = 11
t13 = 8
t23 = 10
a3, b3 = 10, 1
onboard3 = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
# result 20

temperature4 = 11
t14 = 8
t24 = 10
a4, b4 = 10, 100
onboard4 = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
# result 60

print(solution(temperature2, t12, t22, a2, b2, onboard2))