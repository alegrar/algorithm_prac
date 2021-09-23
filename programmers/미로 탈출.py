from collections import deque
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

    switch_dict = [origin_dict, change_dict]
    #print(origin_dict)
    #print(change_dict)
    #print(switch_dict)

    def bfs(start,end,queue):
        switch = 0
        min_w = 3000000 # 3000*1000
        
        while queue:
            print(queue)
            now, w, s  = queue.popleft()
            if now == end :
                min_w = min(min_w, s)
                continue
            if now not in traps: # trap이 아닌 경우 switch 변화 없음
                now_dict = switch_dict[switch%2]
                if now not in now_dict.keys():  
                    continue
                for content in now_dict[now]:
                    node = content[0]
                    weight = content[1]
                    this_content = [node, weight, s+weight]
                    queue.append(this_content)

            else : # trap인 경우
                switch += 1
                if not check[now-1] :
                    now_dict = switch_dict[switch%2]
                    check[now-1] = True
                else :  # 똑같은 trap 방 두 번 방문하면 원래대로 ****
                    now_dict = switch_dict[0]
                    check[now-1] = False
                    switch = 0
                if now not in now_dict.keys():
                    continue
                for content in now_dict[now] :
                    node = content[0]
                    weight = content[1]
                    this_content = [node, weight, s+weight]
                    queue.append(this_content)
        return min_w

    queue = deque()
    check = [False]*n
    # check[start] = True, start는 방문하지 않았다고 보는 게 맞음.
    for contents in origin_dict[start]:
        put_content = []
        put_content.extend(contents) # start에서 시작해서 sum 추가
        put_content.append(contents[1])
        queue.append(put_content)
    answer = bfs(start,end, queue)

    
    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]] 
#roads =  [[1, 2, 2], [3, 2, 3]]
traps = [2, 3]
#traps =  [2]

print(solution(n, start, end, roads, traps))