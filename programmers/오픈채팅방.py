from collections import defaultdict
def solution(record):
    answer = []
    id_dict = defaultdict()
    for content in record:
        total = content.split()
        state = total[0]
        
        if state == 'Enter':
            id = total[1]
            name = total[2]
            id_dict[id] = name
            answer.append([id,state])
        elif state == 'Change':
            id = total[1]
            name = total[2]
            id_dict[id] = name
        else :
            id = total[1]
            answer.append([id,state])
    
    real_answer = []
    for i in answer:
        id, state = i[0], i[1]
        if state == 'Enter':
            real_answer.append(id_dict[id]+'님이 들어왔습니다.')
        else :
            real_answer.append(id_dict[id]+'님이 나갔습니다.')



    return real_answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))