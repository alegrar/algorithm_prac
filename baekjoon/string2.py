# baekjoon # string 19583 # '싸이버개강총회'

from collections import deque

f = open('sample.txt','r')
members = deque()
lines = f.readlines()
for line in lines :
    line = line.strip()
    members.append(line)
    if not line : break
f.close()

S,E,Q = members.popleft().split()
print(S,E,Q)

start_mem = set()
end_mem = set()
print('member list')
S_time = int(''.join(S.split(":")))
E_time = int(''.join(E.split(":")))
Q_time = int(''.join(Q.split(":")))
while members:
    time_, mem = members.popleft().split()
    this_time = int(''.join(time_.split(':')))
    
    if this_time <= S_time:
        start_mem.add(mem)
    if Q_time >= this_time >= E_time:
        end_mem.add(mem)
print(start_mem)
print(end_mem)
answer = start_mem.intersection(end_mem)

print(len(answer))





