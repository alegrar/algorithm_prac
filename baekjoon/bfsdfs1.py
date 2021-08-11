# baekjoon # dfsbfs # 바이러스

cnt = int(input())
couple_cnt = int(input())

# computer_set = set()
# computer_set.add(1)
# for _ in range(couple_cnt):
#     a, b = map(int,input().split())
#     if a in computer_set or b in computer_set :
#         computer_set.add(a)
#         computer_set.add(b)
# print(len(computer_set)-1)

# dfs
# com_dict = {}
# for i in range(1, cnt+1):
#     com_dict[i] = set()

# for i in range(couple_cnt):
#     a, b = map(int,input().split())
#     com_dict[a].add(b)
#     com_dict[b].add(a)

# print(com_dict)
# def dfs(start, com_dict):
#     for i in com_dict[start] :
#         if i not in visited:
#             visited.append(i)
#             dfs(i,com_dict)

# visited = []
# dfs(1,com_dict) # 1에서 시작
# print(visited)
# print(len(visited)-1)

# bfs
from collections import deque
com_dict = {}
for i in range(1, cnt+1):
    com_dict[i] = set()

for i in range(couple_cnt):
    a, b = map(int,input().split())
    com_dict[a].add(b)
    com_dict[b].add(a)

queue = deque()
queue.append(1)
answer = 0
visited = []
while queue :
    now = queue.popleft()
    for i in com_dict[now]:
        if i not in visited :
            queue.append(i)
            visited.append(i)

print(len(visited)-1)
