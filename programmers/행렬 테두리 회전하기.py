def solution(rows, columns, queries):
    answer = []
    board = [[0 for i in range(columns)] for j in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = num
            num += 1
    min_val = rows*columns + 1
    for q in queries:
        start_r, start_c = q[0]-1, q[1]-1
        end_r, end_c = q[2]-1, q[3]-1
        bf_val = board[start_r][start_c]
        min_val = bf_val
        # 제일 위
        for c in range(start_c+1, end_c+1):
            next_val = board[start_r][c]
            board[start_r][c] = bf_val
            bf_val = next_val
            min_val = min(bf_val, min_val)
        # 오른쪽
        for c in range(start_r+1, end_r+1):
            next_val = board[c][end_c]
            board[c][end_c] = bf_val
            bf_val = next_val
            min_val = min(bf_val,min_val)
        # 아래
        for c in range(end_c-1, start_c-1,-1):
            next_val = board[end_r][c]
            board[end_r][c] = bf_val
            bf_val = next_val
            min_val = min(bf_val,min_val)
        # 왼쪽
        for c in range(end_r-1, start_r-1,-1):
            next_val = board[c][start_c]
            board[c][start_c] = bf_val
            bf_val = next_val
            min_val = min(bf_val,min_val)
        #break
        answer.append(min_val)
    # 확인
    return answer

# rows = 6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
rows = 100
columns = 97
queries = [[1,1,100,97]]
print(solution(rows,columns,queries))