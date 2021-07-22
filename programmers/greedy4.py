# 프로그래머스 # greedy # '구명보트'

from collections import deque

# O(n) 으로 끝내야 하는데 더 빡세다. 
# pop(0) : O(n), remove, del 쓰면 안 됨.
# def solution(people, limit):
#     answer = 0
#     while people :
#         rescue_lst = [people[0]]
#         people.pop(0)
#         for person in people:
#             residual = limit - sum(rescue_lst)
#             if person <= residual :
#                 rescue_lst.append(person)
#                 people.remove(person)
    
#         answer += 1
#         rescue_lst = []

#     return answer


# 런타임 에러 안 뜸
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    rescue_lst = []
    while people:
        max_person = people.popleft()
        rescue_lst = [max_person]

        while people :
            residual = limit - sum(rescue_lst)
            min_person = people.pop()
            if residual >= min_person:
                rescue_lst.append(min_person)
            else : 
                people.append(min_person)
                break

        answer += 1

    return answer

people =[70, 80, 50]
# [70, 50, 80, 50] [70, 80, 50], [70,100, 10, 20,30,40, 10, 20, 80, 50]
limit = 100

print(solution(people, limit))