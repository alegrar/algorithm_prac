# 프로그래머스 # hash  #'전화번호 목록'


######################## 효율성 통과 못함
# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book, key = lambda x : len(x))
#     print(phone_book)

#     for prefix in phone_book:
#         phone_book = sorted(phone_book, key = lambda x : len(x))
#         phone_book.pop(0)
#         for str in phone_book :
#             if len(prefix) > len(str) :
#                 break
#             if prefix == str[:len(prefix)] :
#                 print(prefix)
#                 answer = False


#     return answer

# def solution(phone_book):
#     answer = True
#     phone_book.sort()
    
#     for prefix, target in zip(phone_book, phone_book[1:]):
#         #print(p1, p2)
#         if target.startswith(prefix):
#             return False
#     return answer

# 한 번호 전체가 다른 번호의 접두어가 아닌 경우!
def solution(phone_book):
    answer = True
    hash_map = {}
    # sort 사용 안 함.
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    print(hash_map)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            
            if temp in hash_map and temp != phone_number:
                print(temp)
                answer = False
    return answer



phone_book = ["119", "97674223", "1195524421"]
# ["119", "97674223", "1195524421"]
# ["12","123","1235","567","88"]
# ["123","456","789"]
print(solution(phone_book))