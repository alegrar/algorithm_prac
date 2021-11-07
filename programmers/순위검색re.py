from collections import defaultdict
from itertools import combinations
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for content in info:
        c = content.split()
        info_key = c[:-1]
        info_val = int(c[-1])
        for i in range(5): # 인당 다섯 개 조합
            for combi in combinations(info_key,i):
                temp_key = ''.join(combi) # 다 붙인 문자열을 key로, ''도 포함
                info_dict[temp_key].append(info_val)
    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split(' ')
        q_score = int(q[-1])
        q = q[:-1]
        for _ in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q) # info_dict key의 형태로 만들어줌
        
        # lower bound 사용 : 찾고자 하는 값 이상이 처음 나타나는 위치!! (이분탐색 변형)
        if tmp_q in info_dict: #해당 query 조합이 있으면
            scores = info_dict[tmp_q]
            if len(scores) > 0 :
                start, end = 0, len(scores)
                while end > start :
                    mid = (start+end)//2
                    if scores[mid] >= q_score:
                        end = mid
                    else :
                        start = mid + 1
                answer.append(len(scores)-start)
        else :
            answer.append(0)
    
    return answer



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))