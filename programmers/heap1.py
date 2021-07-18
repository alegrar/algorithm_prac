# 프로그래머스 # heap # '더 맵게'

## 시간복잡도 O(NlogN)

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) < 1:
            return -1
        min = scoville[0]
        if min < K:
            min = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min + min2*2)
            answer += 1
        else : 
            return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))
