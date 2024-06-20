# 과제 진행하기
# 2024.06.20
def solution(plans):
    answer = []
    rest = []

    for i in range(len(plans)):
        start_h, start_m = map(int, plans[i][1].split(":"))
        start = start_h * 60 + start_m
        plans[i][1] = start

    plans.sort(key=lambda x : x[1])
    # 이번 과제 끝나는 시간과 다음 과제 시작 시간을 비교
    # 이번 과제 끝나는 시간 <= 다음 과제 시간 시간 => 과제를 끝내고 answer에 append
    # 추가적으로 rest가 비어있지 않는다면 list.pop()을 통해서 최상단 과제를 마무리
    # 이번 과제 끝나는 시간 > 다음 과제 시작 시간 => 남은 시간과 과제 이름을 페어로 rest에 append
    for i in range(len(plans)):
        sub, start, duration = plans[i][0], plans[i][1], int(plans[i][2])
        if i + 1 < len(plans):
            next_start = plans[i+1][1]

            end = start + duration
            if end <= next_start:
                answer.append(sub)
                limit_time = next_start - end

                while rest:
                    if limit_time <= 0:
                        break
                    rest_sub, rest_time = rest.pop()
                    if rest_time <= limit_time:
                        answer.append(rest_sub)
                        limit_time -= rest_time
                    else:
                        rest.append((rest_sub, rest_time - limit_time))
                        break
            else:
                rest.append((sub, end - next_start))

    # 마지막 과제를 answer 추가
    # rest가 비지 않았다면 역순으로 추가
    answer.append(plans[-1][0])
    while rest:
        rest_plan = rest.pop()
        answer.append(rest_plan[0])

    return answer

plans1 = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
plans2 = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
plans3 = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]

print(solution(plans3))