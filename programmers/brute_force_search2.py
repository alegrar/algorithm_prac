#프로그래머스 # 완전탐색 # '소수찾기'
from itertools import permutations

def solution(numbers):
    answer = 0
    num_lst = []
    ans_lst = []
    for i in numbers:
        num_lst.append(i)
    
    for i in range(1, len(num_lst)+1):
        ans_lst.extend(list(permutations(num_lst, i)))


    temp_lst = []
    for val in ans_lst :
        if len(val) <= 1:
            temp_lst.append(val[0])
            continue
        num = ''
        for this in val :
            num += this
        temp_lst.append(num)

    

    # 소수 판정
    temp_lst = list(set(map(int,temp_lst)))


    for val in temp_lst:
        target = int(val)
        if target != 0 and target != 1:
            for i in range(2, target+1) :
                if i == target:
                    answer += 1
                if target % i == 0 :
                    break
                
    return answer



numbers = "213"
# "17"
# "011"
#print(solution(numbers))



########## 에라토스테네스 체

n = 1000
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2,n+1):
    if a[i] :
        primes.append(i) # 일단 넣고 보기 왜냐 어차피 그보다 큰 건 전부 제거되니까
        for j in range(2*i, n+1, i): # 2를 곱한 수 전부 제거 i씩 늘어나면서
            #print(j, end=' ')
            a[j] = False
        print()

print(primes)