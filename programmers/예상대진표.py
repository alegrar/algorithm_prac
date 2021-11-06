def solution(n,a,b):
    answer = 1 
    while True:
        if abs(a-b) == 1 and a//2 != b//2:
            break
        if a%2 != 0 :
            if a == 1 :
                a = 1
            else :
                a += 1
                a //= 2
        else :
            a //= 2

        if b%2 != 0:
            if b == 1:
                b = 1 
            else :
                b += 1
                b //= 2
        else :
            b //= 2
        answer += 1       
        

    return answer

n = 8
a = 4
b = 5
print(solution(n,a,b))
