# 프로그래머스 # 정렬 # 가장 큰 수

## permutations 시간 초과!!!!!!!!!!!!!!!!

from itertools import permutations

# def solution(numbers):
#     answer = ''
#     permu_ = list(permutations(numbers,len(numbers)))
#     temp_answer = list()

#     # 첫째 자리 수 가장 큰 놈 찾기
#     first_num = 0
#     for i in numbers :
#         if first_num <= int(str(i)[0]) :
#             first_num = int(str(i)[0])

    
#     # for per in permu_:
#     #     nums = ''
#     #     if per[0] != first_num :
#     #         continue
#     #     for i in range(len(per)):
#     #         nums += str(per[i])
#     #     if nums not in temp_answer :
#     #         temp_answer.append(int(nums))

#     print(temp_answer)
#     answer = str(max(temp_answer))
#     return answer

def solution(numbers):
    answer = ''
    num = list(map(str,numbers))
    # x*3 : numbers 원소가 1000 이하 이므로 3자리 수 맞추기
    # 문자열 비교는 ascii 값으로 치환되어 정렬하는데
    # 첫번째 인덱스 값으로 비교함.! '9' 가 가장 큼! 
    num.sort(key=lambda x : x*3, reverse=True) 
    # x*3 하는 이유는 30 < 3이 더 크게 될 수 있도록?
    answer = str(int("".join(num)))
    return answer


numbers = [3, 30, 34, 5, 9]
# [6,10,2]
# [3, 30, 34, 5, 9]
print(solution(numbers))