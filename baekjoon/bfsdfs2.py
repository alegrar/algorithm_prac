# baekjoon # dfsbfs # 촌수계산

people_cnt = int(input())
target_a, target_b = map(int,input().split())
couple_cnt = int(input())

people_dict = {}
for i in range(1, people_cnt+1):
    people_dict[i] = set()
for i in range(couple_cnt):
    a, b = map(int, input().split())
    people_dict[a].add(b)
    people_dict[b].add(a)


def dfs(start, cnt, people_dict):
    if start == target_b :
        print(cnt)
        return
    for i in people_dict[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, cnt+1, people_dict)

visited = [target_a]
cnt = 0
dfs(target_a, cnt, people_dict)
if target_b not in visited:
    print(-1)