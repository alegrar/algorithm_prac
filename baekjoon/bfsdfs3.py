# baekjoon # dfsbfs # 숨바꼭질

from collections import deque

N, K = map(int, input().split())
queue = deque()
queue.append([N,0])
visited = [False]*100001
while queue:
    now = queue.popleft()
    val = now[0]
    sec = now[1]
    if not visited[val]:
        visited[val] = True
        if val == K :
            print(sec)
            break
        if val*2 <= 100000: # 중요 메모리 초과
            queue.append([val*2, sec+1])
        if val+1 <= 100000:
            queue.append([val+1, sec+1])
        if val-1 >= 0:
            queue.append([val-1, sec+1])


# 메모리 초과
# N, K = map(int, input().split())
# move_dict = {}
# for i in range(50000):
#     move_dict[i] = set()

# move_dict[0].add(N)

# i = 0
# while True: 
#     if K in move_dict[i]:
#         print(i)
#         break
#     for now in move_dict[i] :
#         move_dict[i+1].add(now*2)
#         move_dict[i+1].add(now-1)
#         move_dict[i+1].add(now+1)
#     i+=1



