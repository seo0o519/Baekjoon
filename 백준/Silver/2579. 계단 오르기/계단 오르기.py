n = int(input())
stair = [int(input()) for _ in range(n)]
stair.insert(0, 0) # 인덱싱 편하게 하기 위해서
memo = [0] * (n+1) 
if n<3:
    print(sum(stair))
else:
    memo[1] = stair[1]
    memo[2] = stair[1]+stair[2]
    for i in range(3, n+1):
         memo[i] = max(memo[i-2] + stair[i], memo[i-3] + stair[i-1] + stair[i])
    print(memo[n])