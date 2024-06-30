# 호텔 대실
# 2024.06.30
# Lv2
from heapq import heappop, heappush
def solution(book_time):
    answer = 1
    book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2])*60 + int(e[3:])) for s, e in book_time]
    book_time.sort()
    heap = []
    for s, e in book_time:
        if not heap:
            heappush(heap, e+10)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap, e+10)
        print(heap)
    return answer

book_time1 = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
book_time2 = [["09:10", "10:10"], ["10:20", "12:20"]]
book_time3 = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time1))