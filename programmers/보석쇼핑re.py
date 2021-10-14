from collections import defaultdict
def solution(gems):
    answer = [0,0]
    min_val = len(gems)+1
    left = 0
    right = 0
    answer_lst = []
    gems_len, set_len = len(gems), len(set(gems))
    gems_dict = defaultdict(lambda:0)
    

    while True: # 처음부터 시작해서 왼쪽 오른쪽을 범위를 맞춰나가게
        now = len(gems_dict)
        if left == gems_len:
            break
        if now == set_len:
            answer_lst.append((left,right))
            gems_dict[gems[left]] -= 1
            if gems_dict[gems[left]] == 0 :
                del gems_dict[gems[left]]
            left += 1
            continue
        if right == gems_len:
            break
        if now != set_len:
            gems_dict[gems[right]] += 1
            right += 1
            continue

    for ans in answer_lst :
        if min_val > ans[1] - ans[0] :
            min_val = ans[1] - ans[0]
            answer = [ans[0]+1 , ans[1]]

    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
#gems = ["XYZ", "XYZ", "XYZ"]
#gems = ["AA", "AB", "AC", "AA", "AC"]
#gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

# def solution(gems):
#     answer = []
#     min_val = len(gems)
#     left = 0
#     right = len(set(gems)) - 1
#     gems_dict = {gem:0 for gem in set(gems)}
#     # dict 초기화
#     for i in range(0,right+1):
#         cnt = gems_dict[gems[i]]
#         gems_dict[gems[i]] = cnt + 1

#     while True: # 한 번에 훑을 수 있음!
#         if left > right or right == len(gems):
#             break
#         else :
#             if 0 in gems_dict.values() : # 0이 하나라도 있으면
#                 right += 1
#                 if right == len(gems) :
#                     continue
#                 cnt = gems_dict[gems[right]]
#                 gems_dict[gems[right]] = cnt + 1
#             else :
#                 if (right - left) < min_val :
#                     min_val = right-left
#                     answer = [left+1, right+1]
#                 left += 1
#                 cnt = gems_dict[gems[left-1]]
#                 gems_dict[gems[left-1]] = cnt - 1


#     return answer





