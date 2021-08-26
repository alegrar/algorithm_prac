#탈옥
# 죄수는 항상 두 명, 각 죄수와 감옥의 바깥을 연결하는 경로는 항상 존재

# bfs로 최소 값 정하기!!

import sys
from collections import deque

#T = sys.stdin.readline()
T = 1
for _ in range(T) :
    N, M = map(int, sys.stdin.readline().split())

    board = ['']*N
    for i in range(N):
        line = list(map(str, sys.stdin.readline().split()))
        board[i] = line

    print(board)