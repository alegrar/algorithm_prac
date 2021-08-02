# baekjoon # string 2577 # '숫자의 개수'

from collections import Counter

A = int(input())
B = int(input())
C = int(input())

target = Counter(str(A*B*C))
for i in range(0, 10):
    print(target[str(i)])

