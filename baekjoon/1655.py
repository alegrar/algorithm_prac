# 가운데를 말해요 # 1655
import heapq

# left는 항상 right보다 작아야 함.
# left = []
# right = []
# n = int(input())

# 1 5 2 10 -99 7 5
# for _ in range(n):
#     num = int(input())
#     if len(left) == len(right): # max_heap
#         heapq.heappush(left,(-num,num))
#     else : # min_heap
#         heapq.heappush(right,(num,num))

#     if right and left[0][1] > right[0][1]:
#         left_val = heapq.heappop(left)[1]
#         right_val = heapq.heappop(right)[1]
#         heapq.heappush(right,(left_val,left_val))
#         heapq.heappush(left,(-right_val, right_val))

#     print(left[0][1])

import heapq
import sys

left, right = [], []
n = int(sys.stdin.readline()) ## sys.stdin.readline 써야함!!!
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left,(-num,num))
    else :
        heapq.heappush(right,(num,num))
    
    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))

    print(left[0][1])


## 시간초과
# N = int(input())
# heap = []
# temp_lst = []
# for i in range(1, N+1):
#     now = int(input())
#     to = i//2
#     temp_lst.append(now)

#     for now in temp_lst:
#         heapq.heappush(heap, now)
#     for j in range(to+1):
#         temp_lst.append(heapq.heappop(heap))
#     if i%2 != 0 :
#         answer = temp_lst.pop()
#         heapq.heappush(heap, answer)
#         print(answer)
#     else :
#         answer1 = temp_lst.pop()
#         answer2 =  temp_lst.pop()
#         heapq.heappush(heap, answer1)
#         heapq.heappush(heap,answer2)
#         print(min(answer1, answer2))
#     while temp_lst:
#         heapq.heappush(heap,temp_lst.pop())


        

