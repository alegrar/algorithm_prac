# 프로그래머스 #dfs bfs #'타겟 넘버'


# 1. bfs
from collections import deque
def solution(numbers, target):
    answer = 0 
    # 나올 수 있는 경우를 queue 에 저장하면서 나아가기
    queue = deque()
    queue.append([1*numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    size = len(numbers)
    while queue:
        now, idx = queue.popleft()
        idx += 1
        if idx < size :
            queue.append([now +1*numbers[idx], idx])
            queue.append([now -1*numbers[idx], idx])
        else :
            if now == target :
                answer += 1

    return answer


# # 2. dfs with recursive
# def solution(numbers, target):
#     n = len(numbers)
#     answer = 0
#     def dfs(idx, result):
#         if idx == n and result == target:
#             nonlocal answer
#             answer += 1
#             return
#         else :
#             # 두 가지 경우를 모두 한번에!
#             dfs(idx+1, result + numbers[idx])
#             dfs(idx+1, result - numbers[idx])
    
#     dfs(0,0) # idx = 0, result = 0
#     return answer



numbers = [1,1,1,1,1]
target = 3

print(solution(numbers, target))