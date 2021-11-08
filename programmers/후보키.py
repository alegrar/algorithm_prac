from collections import defaultdict
from itertools import combinations
def solution(relation):
    answer = 0
    # 학번, 이름, 전공, 학년
    r_dict = defaultdict(set)
    for i in range(1,len(relation[0])+1):
        for combi in combinations(range(len(relation[0])), i):
            r_dict[combi] = 0
    print(r_dict)
    keys = [tuple()]
    for key in r_dict:
        temp = set(tuple())
        for row in relation:
            couple = []
            for i in range(4):
                if i in key:
                    couple.append(row[i])
            temp.add(tuple(couple))
        skip = False
        if len(temp) == len(relation):
            for this_key in keys:
                cnt = 0
                for tk in this_key :
                    for k in key:
                        if len(this_key) == cnt and this_key != ():
                            skip = True
                            break
                        if tk == k:
                            cnt += 1
            if skip :
                continue
            keys.append(key)
            answer += 1

    return answer

relation = [["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]
#relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
relation = [['a','b','c'],['1','b','c'],['a','b','4'],['a','5','c']]
print(solution(relation))