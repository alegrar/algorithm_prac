from collections import deque
def solution(s):
    answer = -1
    stack = deque()
    stack.append(s[0])  
    for i in range(1,len(s)):
        if not stack:
            stack.append(s[i])
            continue
        #print(stack[-1], s[i])
        if stack[-1] == s[i]:
            stack.pop()
        else :
            stack.append(s[i])

    if not stack: 
        answer = 1
    else :
        answer = 0
    return answer
s = 'cdcd'
print(solution(s))


