# baekjoon # dfsbfs # 스타트링크 5014

from collections import deque

F, S, G, U, D = map(int,input().split())

queue = deque([[S,0]])
visited = [False]*1000001

def bfs() : 
    while queue:
        now = queue.popleft()
        floor = now[0]
        cnt = now[1]
        
        if not visited[floor]:
            visited[floor] = True
            if floor == G :
                #print(cnt)
                return cnt
            if floor+U <= F :
                queue.append([floor+U, cnt+1])
            if floor-D >= 1 :
                queue.append([floor-D, cnt+1])
        cnt += 1
    return 'use the stairs'

answer = bfs()
print(answer)