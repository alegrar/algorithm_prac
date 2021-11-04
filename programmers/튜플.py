# import heapq

# def solution(s):
#     answer = set()
#     target = s[1:-1]
#     val_lst = []
#     temp = []
#     end = False
#     val = ''
#     for i in target:
#         if i == '}':
#             val_lst.append(int(val))
#             val = ''
#             cnt = len(val_lst)
#             heapq.heappush(temp,[cnt,val_lst])
#             val_lst = []
#             end = False
#         elif i == '{' :
#             end = True
#         elif i == ',' and end :
#             val_lst.append(int(val))
#             val = ''
#         elif i in '0123456789' :
#             val += i

#     ans = []
#     while temp :
#         now = heapq.heappop(temp)
#         if now[0] == 1 :
#             answer.add(now[1][0])
#             ans.append(now[1][0])
#             continue
#         val = set(now[1]) - answer
#         answer.update(val)
#         ans.append(list(val)[0])
#     return ans




def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')
    
    new_s = []
    for i in s1 :
        new_s.append(i.split(','))
    print(new_s)

    new_s.sort(key=len)
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer



#s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
#s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = "{{20,111},{111}}"
#s = "{{123}}"
#s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))