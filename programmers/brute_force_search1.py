# 프로그래머스 # 완전탐색 # '모의고사'

# def solution(answers):
#     answer = []
#     # pattern 비교하는 게 좋음!
#     no1 = [1,2,3,4,5]*2000
#     no2 = [2,1,2,3,2,4,2,5]*1250
#     no3 = [3,3,1,1,2,2,4,4,5,5] * 1000

#     mem_lst = {1:no1, 2:no2, 3:no3}
#     temp_answer = {}
#     i = 1
#     while i < 4:
#         cnt = 0
#         mem = mem_lst[i]
#         for ans, val in zip(answers, mem):
#             if ans == val :
#                cnt += 1
#         temp_answer[i] = cnt
#         i += 1
    

#     # 이 부분 너무 비효율적 !!! 
#     max = 1
#     for i in range(1, len(temp_answer)+1):
#         if temp_answer[i] > temp_answer[max] :
#             while answer :
#                 answer.pop()
#             max = i
#             answer.append(max)
#         elif temp_answer[i] == temp_answer[max]:
#             answer.append(i)
    
#     return answer




def solution(answers):
    answer = []
    score = [0,0,0]
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    for idx, ans in enumerate(answers):
        if ans == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if ans == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if ans == pattern3[idx % len(pattern3)]:
            score[2] += 1
    
    for i, val in enumerate(score):
        if val >= max(score):
            answer.append(i+1)

    return answer


answers = [1,3,2,4,2]
# [1,2,3,4,5]
# [1,3,2,4,2]
print(solution(answers))