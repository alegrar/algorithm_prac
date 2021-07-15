# 프로그래머스 #hash  #'완주하지 못한 선수'

def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = None

    for part, com in zip(participant, completion):
        print(part,com)
        if part != com :
            answer = part

    if answer == None:
        answer = participant[-1]


    return answer


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# ["leo", "kiki", "eden"]
# ["marina", "josipa", "nikola", "vinko", "filipa"]
# ["mislav", "stanko", "mislav", "ana"]
completion = ["josipa", "filipa", "marina", "nikola"]
# ["eden", "kiki"]
# ["josipa", "filipa", "marina", "nikola"]
# ["stanko", "ana", "mislav"]

print(solution(participant, completion))