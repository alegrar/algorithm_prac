def solution(n, start, end, roads, traps):
    answer = 0
    origin_dict = dict()
    change_dict = dict()
    for road in roads :
        if road[0] in origin_dict.keys():
            new = origin_dict[road[0]]
            new.append([road[1], road[2]])
            origin_dict[road[0]] = new
        else :
            origin_dict[road[0]] = [[road[1], road[2]]]
    for key in origin_dict.keys():
        for node in origin_dict[key]:
            if node[0] not in change_dict.keys() : 
                change_dict[node[0]] = [[key, node[1]]]
            else :
                new = change_dict[node[0]]
                new.append([key,node[1]])
                change_dict[node[0]] = new
    print(origin_dict)
    print(change_dict)
    return answer

n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]

print(solution(n, start, end, roads, traps))