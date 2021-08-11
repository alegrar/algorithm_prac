# baekjoon # dfsbfs # 빙산 2573

from collections import deque
N, M = map(int, input().split())
board = [0]*N
for i in range(N):
    board[i] = list(map(int,input().split()))


total_cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            total_cnt += 1

# 햇수 지날 때마다 빙하녹기
# 덩이 계산

def melt(board,row,col):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    target = board[row][col]
    for i in range(4):
        now_x = row+dx[i]
        now_y = col+dy[i]
        if 0<=now_x <N and 0<=now_y<M and board[now_x][now_y] == 0:
            if target > 0:
                target -= 1
    
    return target

def split(board): # 분리되었는지
    queue = deque()
    residual = []
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                residual.append([i,j])
    total_cnt = len(residual)
    if total_cnt == 0 :
        return 0
    queue.append(residual[0])
    visited = [] 
    for i in range(N):
        visited.append([False]*M)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    while queue :
        now = queue.popleft()
        row, col = now[0], now[1]
        if not visited[row][col] :
            visited[row][col] = True
            cnt += 1
            for i in range(4):
                now_x = row+dx[i]
                now_y = col+dy[i]
                if 0<=now_x<N and 0<=now_y<M and board[now_x][now_y] > 0 :
                    queue.append([now_x,now_y])
    if cnt != total_cnt :
        return -1
    else : 
        return 1


def change_board(board, change_dict):
    for (i,j) in change_dict.keys():
        board[i][j] = change_dict[(i,j)]


year = 0
while True: # 몇년이 걸릴지 모르니까
    
    check = split(board)
    if check == 0 : # 빙하 다 녹은 경우
        print(check)
        break
    elif check == -1: # 빙하 갈라진 경우, 애초에 갈라진 경우
        print(year)
        break

    change_dict = {}
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 :
                val = melt(board,i,j)
                change_dict[(i,j)] = val
    change_board(board, change_dict)
    year += 1
    
    