# 프로그래머스 # 정렬 # k번째수

def solution(array, commands):
    answer = []
    
    for com in commands:
        i, j, k = com[0]-1, com[1], com[2]-1
        target = array[i:j]
        target.sort()
        answer.append(target[k])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))