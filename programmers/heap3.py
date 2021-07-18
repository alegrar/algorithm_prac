# 프로그래머스 # heap # '이중우선순위큐'
import heapq
# heap.remove(max(heap)) list에서 최대값 remove로 제거


# def solution(operations):
#     heap = []

#     for oper in operations:
#         if oper[0] == 'I':
#             heapq.heappush(heap,int(oper[2:]))
#         elif heap :
#             if oper[0] == 'D':
#                 if int(oper[2:]) < 0:
#                     heapq.heappop(heap)
#                 else:
#                     heap.remove(max(heap)) #!!!!!!!!
#     if not heap :
#         return [0,0]

#     return [max(heap), heap[0]]


def solution(operations):
    answer = []
    heap = []
    heap2 = []
    oper_cnt = 0
    insert_cnt = 0 

    for oper in operations:
        this_oper = oper[0]
        if oper_cnt == insert_cnt :
            heap =[]
            heap2 = []
        if this_oper == 'I':
            num = int(oper[2:])
            heapq.heappush(heap, num)
            heapq.heappush(heap2, -num)
            insert_cnt += 1
        elif not heap :
            continue
        elif this_oper == 'D':
            if oper[2:] == '1' :
                heapq.heappop(heap2)
            elif oper[2:] == '-1':
                heapq.heappop(heap)
            oper_cnt += 1
                
    # 비교
    print(heap)
    print(heap2)
    if not heap or not heap2 :
        answer = [0,0]
    else : 
        max_num = - heapq.heappop(heap2) # heap2[0]
        min_num = heapq.heappop(heap) # heap[0]
        answer = [max_num, min_num]


    return answer


operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"] 
# ["I 16","D 1"]
# ["I 7","I 5","I -5","D -1"]
# 1번 케이스 : ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"] 
print(solution(operations))