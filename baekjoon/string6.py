# baekjoon # string # '숫자의 합'

cnt = int(input())
num = input()

answer = 0
for i in range(cnt):
    answer += int(num[i])

print(answer)