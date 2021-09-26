# 방향성 갖는 graph 최소 가중치 간선으로 최소 비용 알고리즘 다익스트라 + 비트마스크
# 간선이 바뀌는 것을 하나의 경로로 판단해서 하기!!
import queue
INF = float('inf')

def dijkstra(n, graph, src, dst, traps):
    pq = queue.PriorityQueue()
    visited = [[False for _ in range(1<<len(traps))] for _ in range(n+1)] # 함정 개수만큼만
    print(visited)
    pq.put((0, src, 0)) # 비용, node, state

    while not pq.empty():
        curr = pq.get()
        w = curr[0]
        node = curr[1]
        state = curr[2]

        if node == dst :
            return w
        if visited[node][state]:
            continue
        visited[node][state] =True

        currTrapped = False # 함정이 발동됐는지
        trapped = {} # 함정이 발동된 노드 저장
        for i in range(len(traps)):
            bit = 1 << i # 1을 index만큼
            if state & bit : # 켜져있다면
                if traps[i] == node:
                    state &= ~bit # 다시 방문한거면 꺼주기
                else :
                    trapped[traps[i]] = True
            else :
                if traps[i] == node:
                    state |= bit
                    trapped[traps[i]] = True
                    currTrapped = True # 현재 노드

        for v in range(1, n+1):
            if v == node :
                continue
            nextTrapped = True if v in trapped else False
            if currTrapped == nextTrapped :
               if graph[node][v] != INF:
                    pq.put((w+graph[node][v], v, state))
            else :
                if graph[v][node] != INF :
                    pq.put((w+graph[v][node], v, state))
    return INF

def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)] #행렬로 표현하기
    for i in range(1, n+1):
            graph[i][i] = 0
    for data in roads:
        u = data[0]
        v = data[1]
        w = data[2]
        if w < graph[u][v] : # 가장 작은 가중치만 필요
            graph[u][v] = w
    #함정노드 방문할 때마다 상태가 바뀜. 비트로 표현
    #priority queue에 (cost, node, state) 형태로 넣기
    #traps의 0번째 인덱스가 발동하면 1로 바꾸기 다시 발동 시 0으로 바꾸기
    return dijkstra(n,graph, start, end, traps)

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]] 
#roads =  [[1, 2, 2], [3, 2, 3]]
traps = [2, 3]
#traps =  [2]

print(solution(n, start, end, roads, traps))