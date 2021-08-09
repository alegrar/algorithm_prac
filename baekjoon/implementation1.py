# baekjoon # implementation 13460 # '구술탈출2'

from collections import deque

N, M = map(int, input().split())

board =  [['']*M for i in range(N)]
for i in range(N):
    now = list(map(str, input()))
    board[i] = now

# 공 위치 저장
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            bx, by = i, j
        if board[i][j] == 'R':
            rx, ry = i, j

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(rx,ry,bx,by):
    queue = deque()
    queue.append((rx,ry,bx,by))
    visited = [] # 방문 여부
    visited.append((rx,ry,bx,by))
    cnt = 0

    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if cnt > 10 : # 10회 초과 시 탈출
                print(-1)
                return
            if board[rx][ry] == 'O': # red가 무사히 구멍에 빠질 시 탈출
                print(cnt)
                return

            for i in range(4):
                now_rx, now_ry = rx, ry
                while True: # 벽이 나오거나 구멍이 나오거나 공이 멈출때까지
                    now_rx += dx[i] # 현재의 방향을 계속 더함
                    now_ry += dy[i]
                    if board[now_rx][now_ry] == '#': # 다음 step이 막혔을 경우
                        now_rx -= dx[i]
                        now_ry -= dy[i]
                        break
                    if board[now_rx][now_ry] == 'O':
                        break
                now_bx, now_by = bx, by
                while True:
                    now_bx += dx[i]
                    now_by += dy[i]
                    if board[now_bx][now_by] == '#':
                        now_bx -= dx[i]
                        now_by -= dy[i]
                        break
                    if board[now_bx][now_by] == 'O':
                        break
                if board[now_bx][now_by] == 'O': # 파란 구슬이 구멍에 들어간 경우 우선 넘기기
                    continue # 파란 구슬이 구멍에 안 들어가고 빨간 구슬이 구멍에 정상적으로 들어갔을 때를 찾기 위해
                if now_rx == now_ry and now_bx == now_by : # 두 구슬의 위치가 같을 경우
                    # 더 많이 이동한 구슬을 한 칸 뒤로!!
                    if abs(now_rx-rx) + abs(now_ry-ry) > abs(now_bx-bx) + abs(now_by-by):
                        now_rx -= dx[i]
                        now_ry -= dy[i]
                    else :
                        now_bx -= dx[i]
                        now_by -= dy[i]

                if (now_rx, now_ry, now_bx, now_by) not in visited:
                    queue.append((now_rx,now_ry,now_bx,now_by))
                    visited.append((now_rx,now_ry,now_bx,now_by))
        cnt += 1
    print(-1) # 실패한 경우

bfs(rx, ry, bx, by)








