# 추억 점수
# 2024.06.20
def solution(name, yearning, photo):
    answer = []
    for picture in photo:
        s = 0
        for p in picture:
            if p in name:
                s += yearning[name.index(p)]
        answer.append(s)
    return answer

name1 = ["may", "kein", "kain", "radi"]
yearning1 = [5, 10, 1, 3]
photo1 = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
# result [19, 15, 6]

name2 = ["kali", "mari", "don"]
yearning2 = [11, 1, 55]
photo2 = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
# result [67, 0, 55]

name3 = ["may", "kein", "kain", "radi"]
yearning3 = [5, 10, 1, 3]
photo3 = [["may"],["kein", "deny", "may"], ["kon", "coni"]]
# result [5, 15, 0]

print(solution(name3, yearning3, photo3))