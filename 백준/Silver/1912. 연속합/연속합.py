N = int(input())
num = list(map(int, input().split()))
memo = [0 for _ in range(N)]
memo[0] = num[0]

for i in range(1,N):
    memo[i] = max(num[i], memo[i-1]+num[i])

print(max(memo))