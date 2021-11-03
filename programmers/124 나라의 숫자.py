# 3진법 변환 코드

def solution(n):
    result = []
    while n :
        t = n % 3 # 1,2,3
        if not t :
            t = 3
            n -= 1 # 나머지가 0이면 -1을 해서 나머지를 3으로 만들어야 함.
        result.append(str(t))
        n //= 3 # 3진법이므로 3보다 작으면 나머지로
    for i in range(len(result)) :
        if result[i] == '3' :
            result[i] = '4'
    answer = ''.join(result[::-1])
    return answer

# 1,2,4
n = 20
# 242
print(solution(n))