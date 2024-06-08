# 주사위 고르기
# 2024.06.06
from itertools import combinations, product
def cal(dice, case):
    A = case
    B = [d for d in dice if d not in A]

    # 합이 될 경우의 수를 모두 구함
    A_total = sorted([sum(i) for i in product(*A)])
    B_total = sorted([sum(i) for i in product(*B)])

    win_games = 0

    for a in A_total:
        win_games += binarySearch(B_total, a)

    return win_games

def binarySearch(case, target):
    left, right = 0, len(case)-1
    while left <= right:
        mid = (left + right) // 2
        if case[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def solution(dice):
    tmp, answer = [], []
    n = len(dice)//2

    # 케이스 전체 분류
    cases = list(combinations(dice, n))
    win = 0

    # 전체 케이스에 대한 승률 계산
    print(cases)
    for case in cases:
        print(case)
        result = cal(dice, case)
        print("result : ", result)
        if result > win:
            tmp = case
            win = result

    for t in tmp:
        for i in range(len(dice)):
            if dice[i] == t:
                answer.append(i+1)
    answer.sort()
    return answer

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
print(solution(dice))