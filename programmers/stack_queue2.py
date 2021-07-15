# 프로그래머스 # stack/hash  #'프린터'

from collections import deque


# def solution(priorities, location):
#     answer = 0
#     change_loc = location

#     if location != 0 and priorities[location] > max(priorities[:location]) :
#         answer = 1
#         return answer
    
#     elif location == 0 and priorities[location] == max(priorities):
#         answer = 1
#         return answer
    
#     else :
#         pri_copy = deque(priorities)
#         while(True):
#             if change_loc == 0 and pri_copy[0] == max(pri_copy):
#                 answer += 1
#                 return answer

#             elif change_loc != 0 and pri_copy[0] == max(pri_copy): 
#                 pri_copy.popleft()
#                 change_loc -= 1
#                 answer += 1
            
#             elif change_loc == 0 and pri_copy[0] != max(pri_copy) :
#                 now = pri_copy.popleft()
#                 pri_copy.append(now)
#                 change_loc = len(pri_copy) - 1
            
#             else:
#                 now = pri_copy.popleft()
#                 pri_copy.append(now)
#                 change_loc -= 1

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    print(queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


priorities = [1, 1, 9, 1, 1, 1]
# [2, 1, 3, 2]
# [1, 1, 9, 1, 1, 1]
location = 0
# 2
# 0
print(solution(priorities, location))