# n+1 카드 게임
# 2024.06.07
# 2024.06.08 해설 참조해서 풀었음 나중에 다시 풀어보면 좋을 듯
from collections import deque
def solution(coin, cards):
    N = len(cards)
    initial = set(cards[:N//3])
    not_yet = deque(cards[N//3:])
    possible = set()

    round = 1
    def update_possible():
        if not_yet:
            possible.add(not_yet.popleft())
            possible.add(not_yet.popleft())
    def remove_pair(source, target):
        nonlocal coin, round
        for x in list(source):
            if N+1-x in target:
                source.remove(x)
                target.remove(N+1-x)
                return True
        return False

    while not_yet:
        update_possible()
        if remove_pair(initial, initial):
            pass
        elif coin >= 1 and remove_pair(initial, possible):
            coin -= 1
        elif coin >= 2 and remove_pair(possible, possible):
            coin -= 2
        else:
            break
        round += 1
    return round

coin1 = 4
coin2 = 3
coin3 = 2
coin4 = 10
cards1 = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
cards2 = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]
cards3 = [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]
cards4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
print(solution(coin4, cards4))