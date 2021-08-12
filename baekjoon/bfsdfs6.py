# baekjoon # dfsbfs # 맥주마시면서 걸어가기 9205

from collections import deque


T = int(input())

for i in range(T):
    beer_cnt = 20
    store_cnt = int(input())
    home = list(map(int,input().split()))
    
    stores = deque()
    for i in range(store_cnt):
        stores.append(list(map(int,input().split())))
    festival = list(map(int,input().split()))
    stores.append(festival)

    # 집과 페스티벌 사이가 맥주 20개로 가능한 경우
    check = False
    if (abs(home[0]-festival[0]) + abs(home[1]-festival[1]))/50 <= 20 :
        print("happy")
        check = True


    def bfs(stores,home,festival):
        visited = [False]*len(stores)
        queue = deque()
        queue.append(home)
        while queue :
            now = queue.popleft()
            if now == festival :
                return 'happy'
            for i in range(len(stores)):
                if not visited[i]:
                    next = stores[i]
                    if (abs(now[0]-next[0]) + abs(now[1]-next[1]))/50 <= 20 :
                        queue.append(next)
                        visited[i] = True
        return 'sad'
        
    if not check :                
        print(bfs(stores,home,festival))

