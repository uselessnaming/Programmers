# 상담원 인원
# 2024.06.19
# 해답 보고 풀었음
# 구현 이지만 조합 후에 어떻게 구해야 할지를 모르겠음
# 최소힙을 이용해서 값을 제외하고 더하고
# retry
from heapq import heappush, heappop
from itertools import combinations_with_replacement, permutations
def solution(k, n, reqs):
    def cal_wait_time(waitings, n):
        total_time = 0
        counsel_list = []
        for _ in range(n):
            heappush(counsel_list, 0)
        for start, duration in waitings:
            prev_end = heappop(counsel_list)
            if start > prev_end:
                heappush(counsel_list, duration)
            else:
                wait_time = prev_end - start
                total_time += wait_time
                heappush(counsel_list, duration + wait_time)
        return total_time
    result = 1e9
    waiting_list = [[] for _ in range(k)]
    for req in reqs:
        waiting_list[req[2] - 1].append([req[0], req[0] + req[1]])

    cases = set()
    for comb in combinations_with_replacement([i for i in range(1, n-k+2)], r=k):
        if sum(comb) == n:
            for perm in permutations(comb, k):
                cases.add(perm)

    for case in cases:
        time = 0
        for i in range(k):
            time += cal_wait_time(waiting_list[i], case[i])
        result = min(result, time)
    return result

k1 = 3
n1 = 5
reqs1 = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
# result 25

k2 = 2
n2 = 3
reqs2 = [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]
# result 90

print(solution(k1, n1, reqs1))