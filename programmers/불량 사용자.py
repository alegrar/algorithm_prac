from collections import defaultdict
def solution(user_id, banned_id):
    answer = 1
    banned = defaultdict(list)

    for no in range(len(banned_id)):
        b_id = banned_id[no]
        for u_id in user_id:
            if len(b_id) == len(u_id):
                cnt = 0
                star = 0
                for i in range(len(b_id)):
                    if b_id[i] == u_id[i]:
                        cnt += 1
                    elif b_id[i] == '*':
                        star += 1
                if cnt + star == len(b_id):
                    banned[no].append(u_id)

    global lst
    lst = []
    def dfs(cnt,s,N):
        global lst
        if cnt == N: #retrun
            if set(s) not in lst:
                lst.append(set(s))
        for cont in banned[cnt]:
            if cont not in s:
                s.append(cont)
                dfs(cnt+1,s,N)
                s.remove(cont)
        return 
    
    dfs(0, list(),len(banned_id))
    print(lst)

    return len(lst)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
#user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
#banned_id =  ["*rodo", "*rodo", "******"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))