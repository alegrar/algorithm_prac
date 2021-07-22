# 프로그래머스 # greedy # '단속 카메라'

# 콩벌레 풀이!!

from collections import deque
def solution(routes):
    answer = 0
    routes.sort()
    queue = deque(routes)

    start, end = queue[0][0], queue[0][1]
    answer += 1    
    while queue:
        if end < queue[0][0] :
            _, end = queue.popleft()
            answer += 1
            continue

        if end > queue[0][1] :
            end = queue[0][1]

        queue.popleft()


    return answer

## 효율성!!!!
# import heapq
# def solution(routes):
#     answer = 0
#     heap = []
#     for route in routes:
#         start = route[0]
#         end = route[1]
#         heapq.heappush(heap,[abs(end-start), start, end])

#     position_lst = []

#     while heap :
#         _, start, end = heapq.heappop(heap)

#         if any(i <= start <= j for i,j in position_lst) :
#             print('1')
#             print(start, end)
#             continue
#         elif any(start<= i <= end for i,_ in position_lst) : 
#             print('2')
#             print(start, end)
#             continue
#         else :
#             print('3')
#             print(start, end)
#             position_lst.append([start,end])
#             answer += 1

#     return answer


routes = [[0,1],[1,2], [2,3]] 
# [[0, 4], [1, 2], [2, 3], [1, 3], [3, 4], [0, 1]] # 2 4?
# [[0, 12], [1, 12], [2, 12], [3, 12], [5, 6], [6, 12], [10, 12]] # 2
# [[-100, 100], [50, 170], [150, 200], [-50, -10], [10, 20], [30, 40]] # 2
# [[ -20, 15], [-14, -5], [-18, -13], [-5, -3 ]] 
# [[0,2],[2,3],[3,4],[4,6]]
# [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15]]
# [[-191, -107], [-184,-151], [-150,-102], [-171,-124], [-120,-114 ]]
print(solution(routes))