# 대충 만든 자판
# 2024.06.28
# Lv1
def solution(keymap, targets):
    answer = []
    alpha = {}

    # dictionary에 최소 값 주입
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in alpha:
                alpha[keymap[i][j]] = j+1
            else:
                if j < alpha[keymap[i][j]]:
                    alpha[keymap[i][j]] = j+1

    # target 마다 매겨진 점수를 answer에 추가
    for target in targets:
        score = 0
        for t in target:
            if t in alpha:
                score += alpha[t]
            else:
                score = -1
                break
        answer.append(score)
    return answer

keymap1, targets1 = ["ABACD", "BCEFD"], ["ABCD","AABB"]
keymap2, targets2 = ["AA"], ["B"]
keymap3, targets3 = ["AGZ", "BSSS"], ["ASA","BGZ"]
keymap4, targets4 = ["ABCDE"], ["FGHIJ"] # -1
keymap5, targets5 = ["ABC"], ["XA"] # -1
keymap6, targets6 = ["ABC"], ["X","X","X"] # -1
keymap7, targets7 = ["BC"], ["AC", "BC"]
keymap8, targets8 = ["ABCDEFGHIJ"], ["JJJJJJJJJJJ"]
keymap9, targets9 = ["BC", "CDB"], ["BB"]
print(solution(keymap1, targets1))