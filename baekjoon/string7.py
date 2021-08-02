# baekjoon # string # 'OX퀴즈'

from collections import deque
cnt = int(input())

for _ in range(cnt):
    quiz = deque(input())
    now_score = 0
    answer = 0
    while quiz:
        result = quiz.popleft()
        if result == 'O':
            now_score += 1
            answer += now_score
        else :
            now_score = 0
    print(answer)