# 프로그래머스 # stack/hash  #'기능 개발'
## indexerror try~except 구문으로 잡을 수도

from collections import deque
import copy
import math

def solution(progresses, speeds):
    answer = []
    days = deque()
    for i, (prog, speed) in enumerate(zip(progresses, speeds)):
        residual = math.ceil((100 - prog)/(speed))
        days.append(residual)


    days_copy = copy.deepcopy(days)
    now = days[0]
    cnt = 0
    while days_copy:
        target = days_copy[0]
        if now >= target:
            cnt += 1
            days_copy.popleft()
            if len(days_copy) == 0:
                answer.append(cnt)
        else : 
            now = target
            answer.append(cnt)
            cnt = 0

    
    return answer

# try :

# except IndexError:
#     answer.append(count)


progresses = [93, 30, 55]
# [93, 30, 55]
# [95, 90, 99, 99, 80, 99]
speeds = [1, 30, 5]
# [1, 30, 5]
# [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))