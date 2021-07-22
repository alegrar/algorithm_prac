# 프로그래머스 # greedy # '섬 연결하기'

## Kruskal : 네트워크의 정점을 최소비용으로 연결
## 사이클이 생성되지 않게 하는 것
## 사이클이 생성되지 않으려면 추가하려는 간선의 양끝점이 같은 집합에 속하지 않아야 함.


def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    node_set = set([costs[0][0]])
    print(costs)

    while len(node_set) != n :
        for i, (_from, _to, cost) in enumerate(costs):
            if _from in node_set and _to in node_set:
                continue
            elif _from in node_set or _to in node_set :
                node_set.update([_from,_to])
                answer += cost
                costs[i] = [-1,-1,-1]
                break
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))