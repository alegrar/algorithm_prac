# 프로그래머스 # dp #'정수 삼각형'

def solution(triangle):
    answer = 0
    size = len(triangle)
    check = []
    for this in triangle:
        check.append([0]*len(this))
    check[0][0] = triangle[0][0]

    for i in range(1, size):
        for j in range(i+1): # i-1행의 j-1 열이랑 j열꺼만 보면 됨
            if 0 < j < i:
                if check[i-1][j-1] >= check[i][j] :
                    check[i][j] = check[i-1][j-1] + triangle[i][j]
                if j <= size and check[i-1][j] + triangle[i][j] >= check[i][j] :
                    check[i][j] = check[i-1][j] + triangle[i][j]
            elif j == 0:
                check[i][j] = check[i-1][j] + triangle[i][j]

            elif j == i :
                check[i][j] = check[i-1][j-1] + triangle[i][j]
    answer = max(check[-1])
        
    
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
