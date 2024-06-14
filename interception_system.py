# 요격 시스템
# 2024.06.14
# Lv2
# 풀이 참고 했음
def solution(targets):
    answer = 0
    bound = 0
    for s, e in sorted(targets):
        if bound > s:
            bound = min(bound, e)
        else:
            bound = e
            answer += 1

    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))