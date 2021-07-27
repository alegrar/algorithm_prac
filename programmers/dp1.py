# 프로그래머스 # DP # 'N으로 표현'
def solution(N, number):
    # initialize 
    total_set = [0,{N}] # 0번째에는 0, N이 한개인 집합 {N} 한 개
    # N이 두개인 집합은 N이 한개인 집합을 두번 합쳐서 조합한 것
    print(total_set)
    if N == number :
        return 1
    for i in range(2,9): # 8단계만 확인하면 됨.
        case_set = {int(str(N)*i)} # N 이어붙인 결과 넣어주고
        for i_half in range(1, i//2+1) : #   
                                               
            for x in total_set[i_half] : # 앞쪽 조합과  ex N=1개 조합
                for y in total_set[i-i_half]: # 뒤쪽 조합 하나씩 섞어서 ex N=2개 조합
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(x*y)
                    case_set.add(y-x) # 뒤에조합에서 
                    if x != 0 :
                        case_set.add(y//x)
                    if y != 0 :
                        case_set.add(x//y)
        if number in case_set:
            return i
        total_set.append(case_set)
    return -1




# 8*8 - 88/8 => 5
N = 5
number = 5
print(solution(N, number))