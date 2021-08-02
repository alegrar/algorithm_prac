# baekjoon # string 1157 # '단어공부'
from collections import Counter
target = input()
target = target.lower()

alpha_cnt = Counter(target)
answer = alpha_cnt.most_common()
if len(answer) > 1 and answer[0][1] == answer[1][1]:
    print('?')
else :
    print(answer[0][0].upper())

