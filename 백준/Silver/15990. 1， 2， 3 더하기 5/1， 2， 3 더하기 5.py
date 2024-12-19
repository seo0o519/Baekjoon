T = int(input())
num = [int(input()) for _ in range(T)]
memo = [[0,0,0] for _ in range(100001)]
memo[1] = [1,0,0]
memo[2] = [0,1,0]
memo[3] = [1,1,1]

for n in range(4,100001):
    memo[n][0] = (memo[n-1][1] + memo[n-1][2]) % 1000000009
    memo[n][1] = (memo[n-2][0] + memo[n-2][2]) % 1000000009
    memo[n][2] = (memo[n-3][0] + memo[n-3][1]) % 1000000009

for i in range(T):
    print((memo[num[i]][0] + memo[num[i]][1] + memo[num[i]][2])% 1000000009)