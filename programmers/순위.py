from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    dic_win = defaultdict(set)
    dic_lose = defaultdict(set)
    for this in results:
        win = this[0]
        lose = this[1]
        dic_win[win].add(lose)
        dic_lose[lose].add(win)

    # 여기서 다시 해줘야 함.
    for i in range(1,n+1):
        for loser in dic_win[i]:
            dic_lose[loser].update(dic_lose[i])
        for winner in dic_lose[i]:
            dic_win[winner].update(dic_win[i])

    print(dic_win)
    print(dic_lose)
    for this in dic_win:
        if len(dic_win[this]) + len(dic_lose[this]) == n-1:
            answer+=1 
    return answer

n = 4
#n = 5
results =  [[1,2],[2,3],[1,4]]
#results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n,results))
