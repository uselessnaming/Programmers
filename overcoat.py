# 덧칠하기
# 2024.06.27
# Lv1
def solution(n, m, section):
    answer = 0

    tmp = []
    for sec in section:
        if tmp:
            if sec >= tmp[0] + m:
                tmp.clear()
                answer += 1
            tmp.append(sec)
        else:
            tmp.append(sec)
    if tmp:
        answer += 1

    return answer

def better_solution(n, m, section):
    answer = 1

    prev = section[0]
    for sec in section:
        if sec >= prev + m:
            prev = sec
            answer += 1

    return answer

n1, m1, section1 = 8, 4, [2,3,6]
n2, m2, section2 = 5, 4, [1,3]
n3, m3, section3 = 4, 1, [1,2,3,4]
print(solution(n3, m3, section3))