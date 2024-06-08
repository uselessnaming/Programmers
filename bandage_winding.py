# PCCP 기출 1번 / 붕대 감기
# 2024.06.08
def solution(bandage, health, attacks):
    #초기 체력
    answer = health

    during_time, heal_s, additional_heal = bandage[0], bandage[1], bandage[2]
    before_time = 0

    # 공격 while 문을 통해서 체력 깍기
    for attack in attacks:
        attack_time, damage = attack[0], attack[1]

        # 힐량 계산
        turn_time = attack_time - before_time - 1
        answer += turn_time * heal_s + (turn_time // during_time) * additional_heal
        if answer > health: answer = health
        # damage 공격
        answer -= damage

        if answer <= 0:
            answer = -1
            break

        before_time = attack_time

    return answer

bandage1 = [5,1,5]
health1 = 30
attacks1 = [[2, 10], [9, 15], [10, 5], [11, 5]]
bandage2 = [3,2,7]
health2 = 20
attacks2 = [[1, 15], [5, 16], [8, 6]]
bandage3 = [4,2,7]
health3 = 20
attacks3 = [[1, 15], [5, 16], [8, 6]]
bandage4 = [1,1,1]
health4 = 5
attacks4 = [[1, 2], [3, 2]]
bandage5 = [1,1,1]
health5 = 20
attacks5 = [[1,5], [4,1]]
bandage6 = [5,1,100]
health6 = 10
attacks6 = [[6,5]]
#result1 : 5 / result2 : -1 / result3 : -1 / result4 : 3
#result5 : 18 / result6 :
print(solution(bandage6, health6, attacks6))