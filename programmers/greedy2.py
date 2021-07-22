# 프로그래머스 # greedy # '조이스틱'

def solution(name):
    change = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    idx = 0
    answer = 0

    print(change)
    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0 :
            return answer

        # 0이 나올 때까지 좌우 이동방향 정하기
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        
        answer += left if left < right else right
        idx += -left if left < right else right


name = "BABAAAAB"
# "JEROEN"
# "JAN"
print(solution(name))
