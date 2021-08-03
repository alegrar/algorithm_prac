# baekjoon # string # '그룹 단어 체커'

from collections import deque

cnt = int(input())
answer = 0
for _ in range(cnt):
    target = deque(input())
    bf_alpha = target.popleft()
    group = set(bf_alpha)
    is_answer = True
    while target :
        alphabet = target.popleft()
        if alphabet != bf_alpha and alphabet in group :
            is_answer = False
            break
        else :
            group.add(alphabet)
            bf_alpha = alphabet
    if is_answer :
        answer += 1

print(answer)

