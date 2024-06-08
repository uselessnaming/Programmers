# 도넛과 막대 그래프
# 2024.06.07
from collections import Counter
def solution(edges):
    answer = [-1,0,0,0]
    input_node = dict()
    output_node = dict()
    # start node를 기준으로 한 edge가 2개 이상인 것들을 찾아야 함
    for edge in edges:
        if edge[0] in output_node:
            output_node[edge[0]] += 1
        else:
            output_node[edge[0]] = 1
        if edge[1] in input_node:
            input_node[edge[1]] += 1
        else:
            input_node[edge[1]] = 1

    total_dict = dict(Counter(input_node) + Counter(output_node))

    for i in total_dict:
        # 출발 노드 계산
        if i not in input_node and output_node[i] >= 2:
            answer[0] = i
        if i in input_node and i in output_node:
            # 8자 그래프 개수 계산
            if output_node[i] == 2 and input_node[i] >= 2:
                answer[3] += 1
        # 막대 그래프 개수 계산
        if i in input_node:
            if input_node[i] >= 1 and i not in output_node:
                answer[2] += 1

    answer[1] = output_node[answer[0]] - (answer[2] + answer[3])

    return answer

edges1 = [[2, 3], [4, 3], [1, 1], [2, 1]]
edges2 = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
edges3 = [[2, 1], [2, 5], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3], [3, 8], [8, 9], [9, 10], [10, 11], [11, 3]]
edges4 = [[2, 1], [1, 3], [2, 4], [4, 5], [2, 6], [6, 7]]
print(solution(edges4))