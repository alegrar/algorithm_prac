# 프로그래머스 # 정렬 # H-index

## citations 인용
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            answer = len(citations) - i
            return answer
    return answer


citations = [0,6,1,5,3]
print(solution(citations))