# 프로그래머스 # hash  #'위장'


# def solution(clothes):
#     answer = 0
#     hash_map = {}
#     key_cnt = 0
#     for key in clothes :
#         if key[1] in hash_map.keys():
#             hash_map[key[1]].append(key[0])
#         else :
#             hash_map[key[1]] = [key[0]]
#             key_cnt += 1 
    
#     #print(hash_map)
#     val_cnt = 0
#     val_lst = []
#     for keys in hash_map.keys():
#         val_cnt += len(hash_map[keys])
#         val_lst.append(len(hash_map[keys]))
 
#     if key_cnt > 1 :
#         permu = 1
#         for cnt in val_lst:
#             permu *= cnt
#         val_cnt += permu
#     answer = val_cnt
#     return answer


def solution(clothes):
    dict = {}
    answer = 0
    for i in clothes : 
        if i[1] in dict : dict[i[1]] += 1
        else : dict[i[1]] = 1
    
    cnt = 1
    for val_cnt in dict.values():
        cnt *= val_cnt + 1 # 모든 경우의 수 !

    answer = cnt-1 # 모두 안 입은 경우, 한 가지 빼기
     

    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))