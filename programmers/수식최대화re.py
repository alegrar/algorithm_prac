# 분할 정복 문제 -> 재귀!!
# 낮은 우선 순위부터 쪼개고, 가장 높은 우선순위까지 쪼갠 후 
# 가장 높은 우선순위부터 계산해 나가기!!
# 
def calculate(priority, n, expression):
    if n == 2: # 가장 높은 우선순위(2)에 도달했을 때 계산
        print(expression)
        return str(eval(expression)) # 식 그대로 계산
    if priority[n] == '*': # 우선순위 낮은 애부터 먼 저 쪼개고 다시 붙임..
        # *를 기준으로 차례대로 식이 나뉘어짐 ex) 100 : 200*300 : 500-20
        # 해당 연산자로 나뉘어질 수 없으면 그대로 숫자만 넘겨짐 eval 은
        # 그 다음에 다시 *를 기준으로 붙여서 계산함.
        # [] 안에는 숫자만 남게 됨.
        res = eval('*'.join([calculate(priority,n+1,e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calculate(priority,n+1,e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calculate(priority,n+1,e) for e in expression.split('-')]))

    return str(res)


def solution(expression):
    answer = 0
    priorities = [
        ('*','-','+'),
        ('*','+','-'),
        ('+','*','-'),
        ('+','-','*'),
        ('-','+','*'),
        ('-','*','+')
    ]
    for priority in priorities:
        res = int(calculate(priority,0,expression))
        answer = max(answer,abs(res))
    return answer

expression = "100-200*300-500+20"
print(solution(expression))

