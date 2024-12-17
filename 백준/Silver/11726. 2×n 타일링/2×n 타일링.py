N = int(input())
memo = [-1 for _ in range(N+1)]
memo[0] = 0

def dp(n):
    if n==1:
        memo[n] = 1
    elif n==2:
        memo[n] = 2
    elif memo[n] == -1:
        memo[n] = dp(n-1) + dp(n-2)

    return memo[n]

dp(N)
print(memo[N]%10007)