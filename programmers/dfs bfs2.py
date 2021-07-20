# 프로그래머스 # dfs bfs # '네트워크'

from collections import deque
def solution(n, computers):

    def bfs(i):
        queue = deque()
        queue.append(i)
        while(queue):
            now = queue.popleft()
            check[now] = 1
            for i in range(n):
                if computers[now][i] == 1 and not check[i] :
                    queue.append(i)
                    
    answer = 0
    check = [0 for i in range(n)] # [0,0,0]
    for i in range(n):
        if not check[i]:
            bfs(i)
            answer += 1
    return answer


# dfs with recursive
# def solution(n, computers):
#     answer = 0
#     check = [0 for i in range(n)]

#     def dfs(node):
#         check[node] = 1
#         for next in range(n):
#             if not check[next] and computers[node][next] == 1:
#                 dfs(next)

#     for node in range(n):
#         if not check[node] :
#             dfs(node)
#             answer += 1

#     return answer    

n = 3 
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))