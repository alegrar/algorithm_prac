# baekjoon # string 6581 # 'HTML'

from collections import deque

sentence = deque()
f = open('sample_html.txt','r')
lines = f.read() # 한의 문자열로 전체가 나옴

line = lines.split()

now_len = 0
for i in line:
    if i == '<br>' :
        print()
        continue
    if i == '<hr>' :
        print()
        print('-'*80)
        now_len = 0
        continue
    if now_len + len(i) > 80:
        print()
        print(i, end=' ')
        now_len = len(i)
    elif now_len + len(i) == 80 :
        now_len += len(i)
        print(i)
        print()
        now_len = 0
    else :
        now_len += len(i)+1
        print(i,end=' ')


f.close()
