# baekjoon # string # '문자열반복'

from collections import deque
T = int(input())

for _ in range(T):
    iter, sentence = input().split()
    answer =''
    sentence = deque(sentence)
    while sentence:
        now_str = sentence.popleft()
        answer += int(iter)*now_str
    
    print(answer)
