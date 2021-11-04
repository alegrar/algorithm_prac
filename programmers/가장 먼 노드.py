from collections import defaultdict, deque
def solution(n, edge):
    answer = 0
    dic = defaultdict()
    for i in range(1,n+1):
        dic[i] = []
    for vertex in edge:
        no1 = vertex[0]
        no2 = vertex[1]
        dic[no1].append(no2)
        dic[no2].append(no1)

    check = [-1 for _ in range(n)]


    def bfs(start):
        count = 0
        queue = deque([[start, count]])
        while queue:
            value = queue.popleft()
            v = value[0]
            count = value[1]
            if check[v-1] == -1:
                check[v-1] = count
                count += 1
                for e in dic[v]:
                    queue.append([e,count])

    bfs(1)
    for value in check:
        if value == max(check):
            answer += 1

    return answer


n = 6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,edge))