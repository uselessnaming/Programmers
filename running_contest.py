# 달리기 경주
# 2024.06.20
# 1차 시간 초과
# 2차 시간 초과
# 3차 시간 초과
# 힌트 봤당 (dict)
def solution(players, callings):
    order = dict()
    for i in range(len(players)):
        order[players[i]] = i

    for calling in callings:
        idx = order[calling]
        order[players[idx]] -= 1
        order[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]

    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))

# 시간 초과
def failed_solution1(players, callings):
    for calling in callings:
        idx = players.index(calling)
        players[idx], players[idx-1] = players[idx - 1], players[idx]
    return players

# 시간 초과
def failed_solution2(players, callings):
    callings_dict = dict()

    for calling in callings:
        if calling in callings_dict:
            callings_dict[calling] += 1
        else:
            callings_dict[calling] = 1

    for calling in callings_dict:
        tmp_idx = players.index(calling)
        tmp = players[tmp_idx]
        for i in range(tmp_idx, tmp_idx-callings_dict[calling], -1):
            players[i] = players[i-1]
        players[tmp_idx - callings_dict[calling]] = tmp

    return players
