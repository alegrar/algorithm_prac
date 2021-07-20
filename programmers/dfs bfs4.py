# 프로그래머스 # dfs bfs # '여행 경로'

def solution(tickets):
    answer = []
    tickets.sort()
    routes = dict()
    
    for s, d in tickets:
        if s in routes:
            routes[s].append(d)
        else:
            routes[s] = [d]

    # stack 활용할 것이므로 사전 순으로 앞선 도착지를 먼저 꺼내도록 내림차순
    for r in routes:
        routes[r].sort(reverse=True)
    #print(routes)


    lst = ['ICN']
    while lst :
        now = lst[-1]
        if now in routes and routes[now]:
            lst.append(routes[now].pop())
            print('여기')
        else :
            print('뇨기')
            answer.append(lst.pop()) # 다 끝났을 때
            
      
    answer.reverse()

    return answer


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))