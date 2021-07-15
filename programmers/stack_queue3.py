# 프로그래머스 # stack/hash  #'다리를 지나는 트럭'

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0] * bridge_length
    while queue :
        answer += 1
        queue.pop(0)
        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight :
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)

    return answer


bridge_length = 100
# 2
# 100
# 100
weight = 100
# 10
# 100
# 100
truck_weights = [10]
# [7,4,5,6]
# [10]
# [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))