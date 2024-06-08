# n+1 카드 게임
# 2024.06.07
from itertools import combinations, product
def solution(coin, cards):
    print(cards)
    answer = 0
    n = len(cards) // 3
    target_number = len(cards) + 1
    index = n
    hand = cards[0:n]
    draw = []
    while index < len(cards):
        # 뽑은 카드들을 draw에 저장
        draw.append(cards[index:index+2])
        index += 2

        # 현재 가지고 있는 카드들의 조합 별 합 경우의 수
        card_comb = list(combinations(hand, 2))
        card_sum = [sum(i) for i in product(*card_comb)]
        for s in card_sum:
            if s == target_number:
                answer += 1
                continue

        # 위의 경우의 수에서 없을 경우 뽑은 카드 + hand에서 조합
        tmp = draw
        for i in hand:
            tmp.append(i)
        print(tmp)
        hand_draw_comb = list(combinations(draw + hand, 2))
        hand_draw_sum = [sum(i) for i in product(*hand_draw_comb)]
        for s in hand_draw_sum:
            if s == target_number:
                coin -= 1
                answer += 1
                continue

        # 위의 경우의 수에서도 없을 경우 draw에서만 조합
        draw_comb = list(combinations(draw, 2))
        draw_sum = [sum(i) for i in product(*draw_comb)]
        for s in draw_sum:
            if s == target_number:
                answer += 1
                continue

    return answer

coin1 = 4
coin2 = 3
coin3 = 2
coin4 = 10
cards1 = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
cards2 = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]
cards3 = [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]
cards4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
print(solution(coin1, cards1))