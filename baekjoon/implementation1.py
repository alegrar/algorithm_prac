# baekjoon # implementation 13460 # '구술탈출2'

from collections import deque
N, M = map(int, input().split())

board =  [['']*M for i in range(N)]
for i in range(N):
    now = list(map(str, input()))
    board[i] = now

# 공 위치 저장
blue, red = deque([0,0]), deque([0,0])
for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            blue = [i,j]
        if board[i][j] == 'R':
            red = [i,j]

# #이 나올 때까지 이동 -> 10번 이하로 위아래 오왼

cnt = 0
answer = 10


def dfs(red, blue, board, cnt, answer):
    if cnt > 10 :
        answer = -1
        return answer
    elif board[red[0]][red[1]] == 'O':
        answer = min(cnt, answer)
        return answer
    
    else :
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for _ in range(10) :
            for x,y in zip(dx,dy):
                now_red = [red[0]+x, red[1]+y]
                now_blue = [blue[0]+x, blue[0]+y]
                if 0 <= now_red[0] < N and 0 <=now_red[1] < M : # red기준
                    if board[now_red[0]][now_red[1]] == '.' or board[now_red[0]][now_red[1]] == 'O':
                        next_x, next_y = 0, 0
                        this_x, this_y = now_red[0], now_red[1]
                        while True: # '#'이 나올 때까지나 B가 나올 때까지
                            if now_red[0] == 1 :
                                next_x += 1
                            elif now_red[0] == -1 :
                                next_x -= 1
                            elif now_red[1] == 1:
                                next_y += 1
                            elif now_red[1] == -1 :
                                next_y -= 1

                            if board[this_x+next_x][this_y+next_y] == '#' or board[this_x][this_y] == 'B':
                                red = [[this_x, this_y]]
                                break
                            elif board[this_x+next_x][this_y+next_y] == 'O':
                                red = [[this_x+next_x][this_y+next_y]]
                                break
                        ###################### blue 처리하기
                        cnt += 1
                        answer = dfs(red,blue,board,cnt,answer)


    return answer

answer = dfs(red, blue, board, 0, 0)


