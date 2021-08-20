# 평범한 배낭 # 12865

N, K = map(int,input().split())

bag = [[0,0]]
total_bag = [[0 for _ in range(K+1)] for _ in range(N+1)] # 4*7
for _ in range(N): 
    weight, value = map(int,input().split()) # 무게, 가치
    bag.append([weight, value])

# 그림 그려서 이해하기!!
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = bag[i][0]
        value = bag[i][1]

        if j < weight :
            total_bag[i][j] = total_bag[i-1][j] # weight 보다 작으면 그 전꺼로

        else :
            # 현재 꺼를 넣고 그 전꺼에서 현재 무게를 뺀 값 더하기 vs 다른 물건들로 채우는 값
            total_bag[i][j] = max(value + total_bag[i-1][j-weight], total_bag[i-1][j])

print(total_bag[N][K])
