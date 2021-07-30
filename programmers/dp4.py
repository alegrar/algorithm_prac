# 프로그래머스 # dp # '도둑질'

## 첫집을 무조건 터는 경우, 마지막집을 무조건 터는 경우
def solution(money):
    answer = 0
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)

    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-2]+money[i], dp1[i-1])
    
    dp2[0] = 0
    dp2[1] = money[1]

    for j in range(2, len(money)):
        dp2[j] = max(dp2[j-2]+money[j], dp2[j-1])

    answer = max(max(dp1), max(dp2))

    return answer


money = [90,0,0,95,1,1] 
# [1,1,4,1,4] 8
# [1000,0,0,1000,0,0,1000,0,0,1000] 3000
# [1000,1,0,1,2,1000,0] 2001
# [1000,0,0,0,0,1000,0,0,0,0,0,1000] 2000
# [1,2,3,4,5,6,7,8,9,10] 30
# [0,0,0,0,100,0,0,100,0,0,1,1] 201
# [11,0,2,5,100,100,85,1] 198
# [1,2,3] 3
# [91,90,5,7,5,7] 104
# [90,0,0,95,1,1] 185
print(solution(money))