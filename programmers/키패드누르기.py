from collections import deque
def solution(numbers, hand):
    answer = ''
    keypad = []
    for i in range(1,12,3):
        keypad.append([i,i+1,i+2])        
    keypad[3][0] = '*'
    keypad[3][2] = '#'
    keypad[3][1] = 0
    #print(keypad)
    right = '#'
    left = '*'

    def calculate(right, left, num):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        rq = deque()
        lq = deque()
        for i in range(4):
            for j in range(3):
                if right == keypad[i][j]:
                    rq.append([i,j,0])
                elif left == keypad[i][j]:
                    lq.append([i,j,0])
        r_min = float('inf')
        l_min = float('inf')
        r_check = []
        l_check = []
        for i in range(4):
            r_check.append([False, False, False])
            l_check.append([False, False, False])

        while rq:
            now = rq.popleft()
            x,y,cnt = now[0], now[1], now[2]
            if keypad[x][y] == num:
                r_min = min(r_min, cnt)
                continue
            for i in range(4):
                row = x+dx[i]
                col = y+dy[i]
                if 0<=row<4 and 0<=col<3 and not r_check[row][col]:
                    #print(keypad[row][col])
                    rq.append([row,col,cnt+1])
                    r_check[row][col] = True

        while lq :
            now = lq.popleft()
            x,y,cnt = now[0], now[1], now[2]
            if keypad[x][y] == num:
                l_min = min(l_min, cnt)
                continue
            for i in range(4):
                row = x+dx[i]
                col = y+dy[i]
                if 0<=row<4 and 0<=col<3 and not l_check[row][col]:
                    lq.append([row,col,cnt+1])
                    l_check[row][col] = True
        if r_min == l_min :
            if hand == 'right':
                return 'R'
            else:
                return 'L'
        elif r_min < l_min :
            return 'R'
        else :
            return 'L'



    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left = num
        elif  num in [3,6,9]:
            answer += 'R'
            right = num
        else :
            answer += calculate(right, left, num)
            if answer[-1] == 'L':
                left = num
            else :
                right = num
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
# 'left'
# 'right'
print(solution(numbers, hand))