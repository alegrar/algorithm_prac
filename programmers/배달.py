from collections import defaultdict, deque
def solution(N, road, K):
    answer = 1
    node = defaultdict(dict)
    for this in road:
        if this[1] in node[this[0]].keys():
            vs = node[this[0]][this[1]]
            node[this[0]][this[1]] = min(vs, this[2])
            node[this[1]][this[0]] = min(vs, this[2])
        else :
            node[this[0]][this[1]] = this[2]
            node[this[1]][this[0]] = this[2]

    check = [False]*N
    check[0] = True
    queue = deque([[1,0]])
    while queue:
        now, w = queue.popleft()
        for next in node[now]:
            if node[now][next]+w <= K and not check[next-1]: 
                queue.append([next,w+node[now][next]])
                check[next-1] = True
                answer += 1
            
    return answer


# 11/10
N = 5
#N = 6
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
#road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K=3
#K=4
print(solution(N,road,K))