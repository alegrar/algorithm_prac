from collections import deque
## 연결리스트 어케할지 고민해보기

def solution(n, k, cmd):
    answer = ''
    left = deque(range(0,k))
    right = deque(range(k,n))
    del_lst = deque()
    
    for now_cmd in cmd :
        if now_cmd[0] == 'U': # 현재 행에서 step만큼 위로
            step = int(now_cmd[2:])
            while step :
                right.appendleft(left.pop())
                step -= 1
        elif now_cmd[0] == 'D': # 현재 행에서 step만큼 아래로
            step = int(now_cmd[2:])
            while step :
                left.append(right.popleft())
                step -= 1
        elif now_cmd[0] == 'C': # 현재 행 삭제 후 바로 아래 행, 마지막행일 경우 바로 윗행
            del_lst.append(right.popleft())
            if not right :
                right.append(left.pop())
        else : # 가장 최근에 삭제된 행을 원래대로 복구
            redo = del_lst.pop()
            if not left and right[0] > redo :
                left.append(redo)
            elif left and right[0] > redo :
                for i in range(len(left)):
                    if left[i] > redo :
                        left.insert(i, redo)
                        break
                if left[-1] < redo :
                    left.append(redo)
            elif not right and left[-1] < redo :
                right.append(redo)
            elif right and right[0] < redo :
                for i in range(len(right)):
                    if right[i] > redo :
                        right.insert(i, redo)
                        break
                if right[-1] < redo :
                    right.append(redo)

                        

    # print(left)
    # print(right)

    total = left
    total += right
    origin = list(range(n))
    i = 0

    for now in total :
        while True: 
            if origin[i] == now :
                answer += 'O'
                i += 1
                break
            else :
                answer += 'X'
                i += 1

    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"] 
#["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

print(solution(n,k,cmd))



