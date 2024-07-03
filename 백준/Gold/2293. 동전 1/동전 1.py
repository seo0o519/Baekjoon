n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

memo = [0] * (k+1) # memo[k] 원을 만들 수 있는 경우의 수 저장 
memo[0] = 1

for i in range(n):
    for j in range(coin[i], k+1):
        memo[j] = memo[j] + memo[j-coin[i]]
print(memo[k])