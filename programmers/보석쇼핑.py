# 효율성테스트 시간초과
from collections import deque
def solution(gems):
    answer = []
    gems_set = set(gems)
    N = len(gems_set)
    for n in range(N, len(gems)+1): # 싹쓸이 할 때 넣을 개수
        basket = deque()
        idx = 0
        for now in gems:
            basket.append(now)    
            idx += 1
            if idx < n :
                continue
            else :
                basket_set = set(basket)
                if len(basket_set) == N :
                    answer.append(idx-n+1)
                    answer.append(idx)
                    break
                basket.popleft()
            
        if len(basket_set) == N:
            break


    return answer



#gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#gems = ["AA", "AB", "AC", "AA", "AC"]
#gems = ["XYZ", "XYZ", "XYZ"]
#gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# gems = ["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"] [3,7]
#gems = ["A","A","A","B","B"] [3,4]
# gems = ["A"] #[1,1]
#gems = ["A","B","B","B","B","B","B","C","B","A"] [8,10]
print(solution(gems))
# idea : 몇개인지 먼저 해서 그 개수부터 차례대로