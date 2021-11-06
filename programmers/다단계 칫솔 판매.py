from collections import defaultdict
def solution(enroll, referral, seller, amount):
    answer = []
    structure = defaultdict(dict)
    structure['-'] = {'end':0}
    for name1, name2 in zip(enroll, referral) :
        structure[name1][name2] = 0

    for who, amt in zip(seller, amount):
        for nm in structure[who]:
            next = nm
        residual = amt*100
        if residual*0.1 >= 1:
            structure[who][next] += residual - residual//10
        residual = residual//10
        while next != '-':
            if residual >= 1:
                now = next
                for nm in structure[now]:
                    next = nm
                structure[now][next] += residual - residual//10
                residual = residual //10
            else :
                break
        if next == '-':
            if residual >= 1:
                residual = residual // 1
                #print(residual)
                structure[next]['end'] += residual
    #print(structure)

    for who in enroll:
        for next in structure[who]:
            res = structure[who][next]
            answer.append(res)
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))