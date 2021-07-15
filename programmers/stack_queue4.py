# 프로그래머스 # stack/hash  #'주식가격'
import copy
from collections import deque

def solution(prices):
    answer = []
    price_copy = deque(prices)

    while price_copy:
        price = price_copy[0]
        _drop = False
        for q2 in price_copy :
            if q2 < price:
                drop_idx = price_copy.index(q2)
                answer.append(drop_idx)
                _drop = True
                break
        if not _drop :
            answer.append(len(price_copy)-1)
        price_copy.popleft()


    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))


# 다른 풀이
# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer





# def solution(prices):
#     answer = []
#     price_copy = deque(prices)

#     while price_copy:
#         price = price_copy[0]
#         try :
#             drop_idx = price_copy.index(price-1)
#             answer.append(drop_idx)

#         except ValueError :
#             answer.append(len(price_copy)-1)
        
#         price_copy.popleft()

#     return answer