# 프로그래머스 # heap # '디스크 컨트롤러'
import heapq


# jobs = [[0, 3], [1, 9], [2, 6]]
# print(solution(jobs))

# 짧은 task를 먼저 해야지 기다리는 시간이 작아짐!! 
# job을 기준으로 하고, 시간이 계속 증가하도록

def solution(jobs):
    answer = 0
    heap = []
    start = -1 # 이미 지나간 거 거르고
    now = 0 # 해당 task 끝나자마자 올 수 있는 거 찾기 위해
    i = 0
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now  :
                heapq.heappush(heap, [job[1], job[0]]) # 우선 순위는 짧은 작업소요시간
        if heap :
            # [해당 시간] 안에 다른 job이 추가될 수 있을지 고려
            this_job = heapq.heappop(heap)
            start = now # 해당 task 마무리 되면 오는 다음 task 최소 시간
            now += this_job[0]
            answer += now - this_job[1]
            i += 1
        else :
            now += 1 # 시간이 흘러서 다음 job이 들어오도록

                
    
    answer = int(answer/len(jobs))
    return answer


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))