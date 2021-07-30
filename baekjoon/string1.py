# baekjoon # string 9935 # '문자열 폭발'


## stack 이용
def solution(sentence, bomb) :
    answer = 'FRULA'
    size_s = len(sentence)
    size_b = len(bomb)
    last_bomb = bomb[-1]
    stack = []
    for char in sentence :
        stack.append(char)
        if char == last_bomb and "".join(stack[-size_b:]) == bomb :
            del stack[-size_b:]
    
    if stack :
        answer = "".join(stack)
    
    return answer

## 시간초과
# def solution(sentence, bomb):
#     answer = 'FRULA'
    
#     while bomb in sentence :
#         sentence = sentence.replace(bomb,'')
    
#     if sentence:
#         answer = sentence

#     return answer


sentence = input().strip()
bomb = input().strip()

# "mirkovC4nizCC44"
# 12ab112ab2ab
# sentence = "mirkovC4nizCC44"
# bomb = "C4"
print(solution(sentence, bomb))