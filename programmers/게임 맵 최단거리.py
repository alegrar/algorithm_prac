from collections import deque
def solution(maps):
    global answer
    answer = float('INF')
    total_len = len(maps)
    row_len = len(maps[0])
    check = [[False for _ in range(row_len)] for _ in range(total_len)]
    def bfs(start):
        queue = deque([start])
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        while queue:
            global answer
            r, c, cnt = queue.popleft()
            if r == total_len-1 and c == row_len-1:
                answer = min(cnt,answer)
                #return
            for i in range(4):
                x = r+dx[i]
                y = c+dy[i]
                if 0<=x<total_len and 0<=y<row_len and not check[x][y] and maps[x][y] == 1:
                    queue.append([x,y,cnt+1])
                    check[x][y] = True

        return

    bfs([0,0,1])
    if answer == float('INF') :
        answer = -1

    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))