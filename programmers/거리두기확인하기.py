def solution(places):
    answer = []
    
    def bfs(r,c,now):
        dx = [1,-1,0,0,1,-1,1,-1,2,-2,0,0]
        dy = [0,0,1,-1,1,-1,-1,1,0,0,2,-2]

        check = []
        for i in range(12):
            row = r+dx[i]
            col = c+dy[i]
            if 0<=row<5 and 0<=col<5 and now[row][col] == 'P':
                check.append([dx[i],dy[i]])
        print(check)
        check2 = False
        for (x,y) in check:
            if x == 2 or y == 2 or x == -2 or y == -2 :
                if x == 2:
                    if now[r+1][c+0] == 'X':
                        check2 = True
                elif y == 2:
                    if now[r+0][c+1] == 'X':
                        check2 = True
                elif x == -2 :
                    if now[r-1][c+0] == 'X':
                        check2 = True
                elif y == -2 :
                    if now[r+0][c-1] == 'X':
                        check2 = True
                else :
                    return 0
                
            else :
                if now[r+0][c+y] == 'X' and now[r+x][c+0] == 'X':
                    check2 = True
                    continue
                else :
                    return 0

        if check2 :
            return 1
        if check == [] :
            return 1
        else :
            return 0

    for now in places:
        temp = []
        for i in range(5):
            for j in range(5):
                if now[i][j] == 'P':
                    temp.append((i,j))
        check2 = []
        for r,c in temp :
            ans = bfs(r,c,now)
            if ans == 0 :
                answer.append(0)
                break
            check2.append(ans)
        if len(check2) == len(temp) :
            answer.append(1)

    
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))