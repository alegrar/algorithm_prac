#탈옥
# 죄수는 항상 두 명, 각 죄수와 감옥의 바깥을 연결하는 경로는 항상 존재

# bfs로 최소 값 정하기!!

import sys
from collections import deque

T = sys.stdin.readline()
for _ in range(int(T)) :
    N, M = map(int, sys.stdin.readline().split())

    board = [0]*N
    for i in range(N):
        line = list(map(str, sys.stdin.readline()))
        next = []
        for j in range(M):
            next.append(line[j])
        board[i] = next

    person = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == '$' :
                person.append((i,j))
    

    ## 동시에 해야함!!!!ㅠㅠㅠㅠ
    
    def bfs(r,c):
        queue = deque()
        queue.append([r,c,0,[]]) # row, col, door count, doors
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        cnt = 0
        min_val = M*N
        check = [[False]*M for _ in range(N)]
        min_doors = []

        while queue:
            row, col, cnt, doors = queue.popleft()
            if row == 0 or row == N-1 or col == 0 or col == M-1 : # 탈출
                if min_val > cnt :
                    min_val = cnt
                    min_doors = doors
            for i in range(4):
                x = row + dx[i]
                y = col + dy[i]
                if 0<=x<N and 0<=y<M and not check[x][y] and board[x][y] != '*' :
                    now_cnt = cnt
                    now_doors = doors[:]
                    if board[x][y] == '#':
                        now_cnt += 1
                        now_doors.append((x,y))
                    queue.append([x,y,now_cnt,now_doors])
                    check[x][y] = True
        return min_val, min_doors



    check = [[False]*M for _ in range(N)]
    answer = set()
    for (r,c) in person:
        this_min, this_doors = bfs(r,c)
        answer.update(this_doors)
    print(len(answer))