# 가장 많이 받은 선물
# 2024.06.08
def solution(friends, gifts):
    answer = [0 for _ in range(len(friends))]

    # 주고 받은 선물에 대한 정보
    gift_infos = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    gifts_score = []

    # 주고 받은 선물에 대한 정보 기록
    for gift in gifts:
        give, get = gift.split()
        gift_infos[friends.index(give)][friends.index(get)] += 1

    # 선물 지수 계산
    for i in range(len(friends)):
        give, get = 0, 0
        for gift_info in gift_infos:
            get += gift_info[i]
        for gift in gift_infos[i]:
            give += gift
        gifts_score.append(give - get)

    # 주고 받지 않은 경우에는 선물 지수를 비교하여 추가해야 함
    # 완전 탐색해서 [i, j]와 [j, i]를 비교해서 해야 함
    for i in range(len(gift_infos)):
        for j in range(len(gift_infos)):
            if i < j:
                # 둘 다 0 이면 선물 지수를 비교해야 함
                if gift_infos[i][j] == gift_infos[j][i]:
                    if gifts_score[i] > gifts_score[j]:
                        answer[i] += 1
                    elif gifts_score[j] > gifts_score[i]:
                        answer[j] += 1
                elif gift_infos[i][j] > gift_infos[j][i]:
                    answer[i] += 1
                elif gift_infos[j][i] > gift_infos[i][j]:
                    answer[j] += 1

    return max(answer)

friends1 = ["muzi", "ryan", "frodo", "neo"]
gifts1 = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
friends2 = ["joy", "brad", "alessandro", "conan", "david"]
gifts2 = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
friends3 = ["a", "b", "c"]
gifts3 = ["a b", "b a", "c a", "a c", "a c", "c a"]
# 1 >> 2 / 2 >> 4 / 3 >> 0
print(solution(friends3, gifts3))