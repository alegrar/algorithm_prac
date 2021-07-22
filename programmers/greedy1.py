# 프로그래머스 # greedy # '체육복'

# reserve 기준 왼쪽부터 local optimum 찾기

def solution(n, lost, reserve):
    answer = 0
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i-1 in set_lost :
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    answer = n - len(set_lost)
    return answer


n = 5
# 5, 5, 3
lost = [2,4]
# [2,4] [2,4] [3]
reserve = [1,3]
# [1, 3, 5] [3] [1]

print(solution(n, lost, reserve))