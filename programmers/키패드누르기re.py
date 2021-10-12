from collections import deque
def solution(numbers, hand):
    answer = ''
    keypad = []
    for i in range(1,12,3):
        keypad.append([i,i+1,i+2])     
    keypad[3][0] = '*'
    keypad[3][2] = '#'
    keypad[3][1] = 0

    keypad = dict()
    for i in range(1,10,3):
        keypad[i] = [i//3,0]
        keypad[i+1] = [i//3,1]
        keypad[i+2] = [i//3,2]
    keypad['*'] = [3,0]
    keypad[0] = [3,1]
    keypad['#'] = [3,2]
    # print(keypad)

    right = keypad['#']
    left = keypad['*']
    numbers = deque(numbers)
    while numbers:
        num = numbers.popleft()
        r,c = keypad[num]

        if num in [1,4,7]:
            answer += 'L'
            left = keypad[num]
        elif num in [3,6,9]:
            answer += 'R'
            right = keypad[num]
        else :
            if (abs(right[0]-r) + abs(right[1]-c)) > (abs(left[0]-r)+ abs(left[1]-c)):
                answer += 'L'
                left = keypad[num]
            elif (abs(right[0]-r) + abs(right[1]-c)) < (abs(left[0]-r)+ abs(left[1]-c)):
                answer += 'R'
                right = keypad[num]
            else : # 같을 경우
                if hand == 'right':
                    answer += 'R'
                    right = keypad[num]
                else :
                    answer += 'L'
                    left = keypad[num]


    
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
# 'left'
# 'right'
print(solution(numbers, hand))