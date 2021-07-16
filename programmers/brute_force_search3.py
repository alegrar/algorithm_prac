#프로그래머스 # 완전탐색 # '카펫'

def solution(brown, yellow):
    answer = []
    i, j = 0,0
    while i < brown :
        i += 1
        j = 1
        while j < brown :
            j += 1
            if 2*(i+j)-4 == brown :
                if i*j - brown == yellow :
                    if i >= j :
                        answer.extend([i,j])
                    else :
                        answer.extend([j,i])
                    return answer

brown =24
# 10 8 24 # 8이상 5000 이하
yellow = 24
# 2 1 24 # 1 이상 2000000 이하
print(solution(brown, yellow))