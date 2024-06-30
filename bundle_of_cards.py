# 카드 뭉치
# 2024.06.30
# Lv1
def solution(cards1, cards2, goal):
    bef_card1 = -1
    bef_card2 = -1
    for card in goal:
        if card in cards1:
            if cards1.index(card) != bef_card1+1:
                return "No"
            bef_card1 += 1
        elif card in cards2:
            if cards2.index(card) != bef_card2+1:
                return "No"
            bef_card2 += 1
    return "Yes"

cards11, cards12 = ["i", "drink", "water"], ["want", "to"]
goal1 = ["i", "want", "to", "drink", "water"]

cards21, cards22 = ["i", "water", "drink"], ["want", "to"]
goal2 = ["i", "want", "to", "drink", "water"]

cards31 = ["show", "lot", "please", "the", "me"]
cards32 = ["money"]
goal3 = ["show", "me", "the", "money"]

print(solution(cards11, cards12, goal1))