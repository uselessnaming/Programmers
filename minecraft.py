# 광물 캐기
# 2024.06.21
# Lv2
# 순서를 바꾸면 안됨!!!
# 알고리즘 방향은 맞음
def solution(picks, minerals):
    answer = 0
    s = sum(picks) * 5

    if len(minerals) > s:
        minerals = minerals[:s]

    # 5개씩 끊어서 dia / iron / stone 많은 순으로 정렬
    temp = [[0,0,0] for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            temp[i//5][0] += 1
        elif minerals[i] == "iron":
            temp[i//5][1] += 1
        else:
            temp[i//5][2] += 1

    temp.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    print(temp)

    for mineral in temp:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p] > 0:
                picks[p] -= 1
                answer += d + i + s
                break
            elif p == 1 and picks[p] > 0:
                picks[p] -= 1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p] > 0:
                picks[p] -= 1
                answer += 25*d + 5*i + s
                break

    return answer

picks1 = [1, 3, 2]
minerals1 = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
# result 12

picks2 = [0, 1, 1]
minerals2 = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
# result 50

print(solution(picks2, minerals2))