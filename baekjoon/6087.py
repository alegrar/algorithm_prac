# 레이저 통신
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

board = [0]*N
for i in range(N):
    line = list(map(str, sys.stdin.readline()))
    next = []
    for j in range(M):
        next.append(line[j])
    board[i] = next

C = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 'C' :
            C.append((i,j))

def bfs(r,c):
    queue = deque()
    queue.append((r,c,-1,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check = [[False]*M for _ in range(N)]
    min_val = M*N
    check[r][c] = True

    while queue:
        row, col, dir, cnt = queue.popleft()
        if board[row][col] == 'C' and (row,col) in C :
            min_val = min(min_val, cnt)

        for i in range(4): # 0,1 위 아래 2,3 오른쪽 왼쪽
            x = row + dx[i]
            y = col + dy[i]
            
            if 0<=x<N and 0<=y<M and not check[x][y] and board[x][y] != '*':
                this_cnt = cnt
                this_dir = dir
                if this_dir in [0,1] and i in [2,3] :
                    this_cnt += 1
                    this_dir = i
                elif this_dir in [2,3] and i in [0,1]:
                    this_cnt += 1
                    this_dir = i
                if dir == -1 :
                    this_dir = i
                queue.append((x,y,this_dir,this_cnt))
                check[x][y] = True

    return min_val

answer = 0
r,c = C.pop()
answer = bfs(r,c)
print(answer)