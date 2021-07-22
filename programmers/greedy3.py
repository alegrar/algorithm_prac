# 프로그래머스 # greedy # '큰 수 만들기'


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0 :
            print(stack)
            k -= 1 
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

# 런타임 에러, 시간 초과
# def solution(number, k):
#     target_lst = list(map(str,number))
#     check = [0]*len(number)

#     def dfs(num_lst, max, standard):
#         if len(num_lst) == len(number) - k :
#             final_num = int(num_lst)
#             if max < final_num :
#                 max = final_num
#             return max
#         else :
#             for i in range(len(target_lst)) :
#                 if not check[i] and standard <= i:
#                     check[i] = 1
#                     standard = i
#                     max = dfs(num_lst+target_lst[i], max, standard)
#                     check[i] = 0

#         return max
#     num_lst = ''
#     max = 0
#     answer = dfs(num_lst, max, 0)
#     answer = str(answer)
#     return answer



number = "4177252841"
# "1924" "1231234" "4177252841"
k = 3
print(solution(number, k))
# 런타임 에러
