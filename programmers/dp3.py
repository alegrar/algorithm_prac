# 프로그래머스 # dp # '등굣길'

## 도착하지 못한 경우 포함

def solution(m, n, puddles):
    answer = 0
    square = [[0]*(m+1) for i in range(n+1)] # 0행0열 만들어두기 -> 계산용이
    square[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1 :
                continue
            if [j, i] in puddles:
                square[i][j] = 0
            else : 
                square[i][j] = square[i-1][j] + square[i][j-1]

    answer = square[n][m]
    
    return answer



## bfs
# from collections import deque
# def solution(m, n, puddles):
#     answer = 0
#     puddles_rev = []
#     for i in puddles :
#         puddles_rev.append([i[1]-1, i[0]-1])
    
#     def bfs(answer):
#         queue = deque([[0,0,0]])
#         step_row = [1, 0]
#         step_col = [0, 1]
#         min_val = 10000
#         while queue :
#             this_node = queue.popleft()
#             x, y, cnt = this_node[0], this_node[1], this_node[2]
#             for i in range(2):
#                 next_row = x + step_row[i]
#                 next_col = y + step_col[i]
#                 if  0 <= next_row < n and 0 <= next_col < m and [next_row, next_col] not in puddles_rev:
#                     queue.append([next_row, next_col, cnt+1])
#                 if next_row == n-1 and next_col == m-1 :
#                     if min_val >= cnt :
#                         min_val = cnt
#                         answer += 1
#         return answer
#     answer = bfs(answer)%1000000007
    
#     return answer

m = 4
n = 3
puddles = [[2,2]]
print(solution(m,n,puddles))