from itertools import permutations 
def solution(expression):
    answer = 0
    opr_set = set()
    for opr in expression :
        if opr in ['+','-','*']:
            opr_set.add(opr)
    #print(opr_set)
    order = list(map(''.join, permutations(opr_set,3) ))
    print(order) # ['*-+', '*+-', '-*+', '-+*', '+*-', '+-*']



    # 다시 차근차근
    def calculate(opr,exp): # 0~999
        for idx in idx_lst :
            print(exp[idx])
            front_idx = idx -1
            back_idx = idx + 1
            _front, _back = False, False
            if exp[front_idx] == ')' :
                _front = True
            if exp[back_idx] == '(':
                _back = True
            while not _front and front_idx >= 0 and exp[front_idx] in '0123456789':
                front_idx -= 1
            while _front and front_idx >= 0 and exp[front_idx] != '(' :
                front_idx -= 1
            while not _back and back_idx < len(exp) and exp[back_idx] in '0123456789':
                back_idx += 1
            while _back and back_idx < len(exp) and exp[back_idx] != ')':
                back_idx += 1
            print('check', exp[front_idx+1], exp[back_idx-1])


            if front_idx >= 0 and  exp[front_idx] == '(' : # 괄호빼고
                front_num = int(exp[front_idx+1:idx-1])
            elif front_idx < 0 :
                front_num = int(exp[front_idx+1:idx])
            else : # 괄호없는 경우
                front_num = int(exp[front_idx+1:idx])

            if back_idx < len(exp) and exp[back_idx] == ')' :
                exp[idx:back_idx-1]
                back_num = int(exp[idx+2:back_idx-1])
            elif back_idx == len(exp):
                back_num = int(exp[idx+1:back_idx-1])
            else :
                back_num = int(exp[idx+1:back_idx-1])
            print('front num, back_num')
            print(front_num, back_num)
            value = 0
            if opr == '*':
                value = front_num * back_num
            elif opr == '+':
                value = front_num + back_num
            else :
                value = front_num - back_num
            
            origin = exp[front_idx:back_idx]
            print('origin ',origin)
            change = '('+str(value)+')'
            new_exp = exp.replace(origin, change)
            print(new_exp)
        return new_exp


    answer_lst = []
    for ordering in order:
        new_exp = expression[:]
        for opr in ordering: # *+-
            idx_lst = []
            for now in range(len(new_exp)) :
                if new_exp[now] == opr:
                    idx_lst.append(now)
            new_exp = calculate(opr, new_exp)
        answer_lst.append(abs(int(new_exp)))


    return answer

expression = "100-200*300-500+20"
# "50*6-3*2"
print(solution(expression))