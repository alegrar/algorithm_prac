class Node : 
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n,k,cmd):
    nodeArr = [Node() for _ in range(n)]
    for i in range(1,n):
        nodeArr[i-1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i-1]

    curr = nodeArr[k]
    stack = []

    for str in cmd :
        if str[0] == 'U':
            step = str[2:]
            for _ in range(step):
                curr = curr.prev
        elif str[0] == 'D':
            step = str[2:]
            for _ in range(step):
                curr = curr.next
        elif str[0] == 'C':
            stack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up :
                up.next = down
            if down :
                down.prev= up
                curr = down
            else :
                curr = up # 마지막 행일 경우 위에것으로
        else :
            node = stack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up :
                up.next = node
            if down :
                down.prev = node
            
    answer = ''
    for i in range(n):
        if nodeArr[i].removed:
            answer += 'X'
        else :
            answer +='O'
    return answer