

#효율성 x
def solution(info, query):
    answer = []
    info_lst = []
    for content in info:
        info_lst.append(content.split())
    #print(info_lst)
    for q in query:
        q = q.split(' and ')
        last = q[3].split(' ')
        q.pop()
        q.append(last[0])
        q.append(last[1])
        ans = 0
        for i in info_lst:
            cnt = 0
            for j in range(5):
                if j == 4 and int(q[j]) <= int(i[j]) :
                    cnt += 1
                else :
                    if q[j] == i[j] or q[j] == '-':
                        cnt += 1
            if cnt == 5:
                ans += 1
        answer.append(ans)

                
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))