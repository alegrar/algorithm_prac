from collections import deque
def solution(board):
    answer = 0
    check = []
    N = len(board)
    check = [[False for _ in range(N)] for _ in range(N)]

    _type = 'r' 
    global min_val
    min_val = float('INF')

    check[0][0] = True
    def dfs(r,c,t,cost):
        global min_val
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        if r == N-1 and c == N-1 :
            #print(r,c,cost)
            min_val = min(min_val, cost)
            return
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]
            if 0<=x<N and 0<=y<N and not check[x][y] and board[x][y] != 1:
                #print(x,y,t,cost) # 2, 0, c, 100
                check[x][y] = True
                if r == 0 and c ==0 :
                    if r-x == 0 :
                        dfs(x,y,'r',100)
                    elif c-y == 0:
                        dfs(x,y,'c',100)
                else :
                    if r-x==0 and t=='r' :
                        dfs(x,y,'r',cost+100)
                    elif r-x==0 and t=='c':
                        dfs(x,y,'r',cost+600)
                    elif c-y==0 and t=='c':
                        dfs(x,y,'c',cost+100)
                    elif c-y==0 and t=='r':
                        dfs(x,y,'c',cost+600)
                check[x][y] = False
        return 

    dfs(0,0,_type,0)
    answer = min_val

    return answer


#board = [[0,0,0],[0,0,0],[0,0,0]]
#board= [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
#board =  [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

print(solution(board))