def solution(s):
    answer = 0
    # one, two, three, four, five, six, seven, eight, nine, zero
    temp = []
    skip = 0
    for i in range(len(s)):
        if s[i] in '0123456789':
            temp.append(s[i])
        else :
            if skip != 0 :
                skip -= 1
                continue
            if s[i] == 'o':
                temp.append('1')
                skip = 2
            elif s[i] == 't':
                if s[i+1] == 'w':
                    temp.append('2')
                    skip = 2
                if s[i+1] == 'h':
                    temp.append('3')
                    skip = 4
            elif s[i] == 'f':
                if s[i+1] == 'o':
                    temp.append('4')
                    skip = 3
                if s[i+1] == 'i':
                    temp.append('5')
                    skip = 3
            elif s[i] == 's':
                if s[i+1] == 'i':
                    temp.append('6')
                    skip = 2
                if s[i+1] == 'e':
                    temp.append('7')
                    skip = 4
            elif s[i] == 'e':
                temp.append('8')
                skip = 4
            elif s[i] == 'n':
                temp.append('9')
                skip = 3
            else :
                temp.append('0')
                skip = 3
    #print(temp)
    answer = ''.join(temp)
    return int(answer)


s = "123"
print(solution(s))