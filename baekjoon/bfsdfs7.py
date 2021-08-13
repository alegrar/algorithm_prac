# baekjoon # dfsbfs # 로봇청소기 14503

from collections import deque

N, M = map(int, input().split())
r,c,d = map(int, input().split())

board = [0]*N
for i in range(N):
    board[i] = list(map(int,input().split()))

## 조건
# 1) 왼쪽방향으로 회전 후 한 칸 전진 청소.
# 2) 왼쪽방향에 청소할 공간이 없으면 그방향으로 회전
# 3) 네 방향 모두 청소가 이미 되어있거나 벽인 경우, 한 칸 후진
# 4) 네 방향 모두 청소가 이미 되어있거나 벽이면서 뒤쪽도 벽이면 작동 멈춤

def check_four(now, board, visited):
    # 북동남서 0123
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dir = now[2]
    check = 0
    back = True
    for i in range(4):
        row = now[0]+dx[i]
        col = now[1]+dy[i]
        if board[row][col] == 1 or visited[row][col] : 
            check +=1
            # 뒤쪽이 막힌 건지 체크
            if i < 2 and i == dir-2 :
                back = False
            elif i >=2 and i == dir+2:
                back = False
    if check == 4 and not back:
        return 'd'
    elif check == 4 and back :
        return 'c'


def bfs(board,r,c,d):
    queue = deque()
    queue.append((r,c,d))
    cnt = 1
    visited = [False]*N
    for i in range(N):
        visited[i] = [False]*M

    # 북동남서 0123
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue :
        now = queue.popleft()
        visited[now[0]][now[1]] = True
        check = check_four(now, board, visited)
        if check == 'c' : # 한 칸 후진
            print('c')
            if now[2] == 0 :
                change_dir = now[2]+2
                queue.append((now[0]+2, now[1], change_dir))
            elif now[2] == 1:
                change_dir = now[2]+2
                queue.append((now[0], now[1]+2, change_dir))
            elif now[2] == 2:
                change_dir = now[2]-2
                queue.append((now[0]-2, now[1], change_dir))
            else :
                change_dir = now[2]-2
                queue.append((now[0], now[1]-2, change_dir))
            continue

            
        elif check == 'd' : # 작동 멈춤
            print('d')
            return cnt
        
        
        # 왼쪽 체크
        now_dir = now[2] - 1
        if now_dir < 0 : now_dir = 3
        dir_lst = [now_dir, now_dir-1, now_dir-2, now_dir-3] 
        for i in dir_lst :
            row = now[0] + dx[i]
            col = now[1] + dy[i]
            if i<0 : i+=4
            dir = i
            if 0<=row<N and 0<=col<M and board[row][col] != 1 and not visited[row][col] : # a
                print('a')
                queue.append((row,col,dir))
                print(row,col,dir)
                visited[row][col] = True
                cnt += 1


            #     break
            # elif board[row][col] != 1 and visited[row][col]: # b
            #     print('b')
            #     i = i-1 # 왼쪽으로 방향만 바꾸기
            #     print(row,col,dir)
            # else:
            #     print(row,col,dir)
            #     i = i-1 # 왼쪽으로 방향만 바꾸기

print(bfs(board,r,c,d))
        