from collections import defaultdict
from itertools import combinations
def solution(relation):
    answer = 0
    # 학번, 이름, 전공, 학년
    r_dict = defaultdict(set)
    for i in range(1,len(relation[0])+1):
        for combi in combinations(range(len(relation[0])), i):
            r_dict[combi] = 0
    # print(r_dict)
    keys = []
    for key in r_dict:
        temp = set(tuple())
        for row in relation:
            couple = []
            for i in range(len(relation[0])):
                if i in key:
                    couple.append(row[i])
            temp.add(tuple(couple))
        #print(temp)
        # 후보키인지 판단
        if len(set(temp)) == len(relation):
            turn = True
            if keys == []:
                keys.append(key)
                continue
            for now in keys:
                if set(now).issubset(set(key)):
                    turn = False
                    break
            if turn:
                keys.append(key)
                #print(keys)

    answer = len(keys)
    return answer

#relation = [["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
#relation = [['a','b','c'],['1','b','c'],['a','b','4'],['a','5','c']]
print(solution(relation))