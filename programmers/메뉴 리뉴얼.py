from itertools import combinations # 개수가 엄청 적음
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course: # 2,3,4
        temp = []
        for order in orders:
            comb = combinations(sorted(order),c)
            temp += comb
        cnt = Counter(temp)
        if len(cnt) != 0 and max(cnt.values()) != 1:
            for f in cnt :
                if cnt[f] == max(cnt.values()):
                    answer += [''.join(f)]

    return sorted(answer)

# {'A': [0, 1, 3, 5], 'B': [0, 4], 'C': [0, 1, 2, 3, 4, 5], 
# 'F': [0, 4], 'G': [0, 4], 'D': [2, 3, 5], 'E': [2, 3, 5], 'H': [5]}
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]  # 2~20
course = [2,3,4]
print(solution(orders,course))