N = int(input())
price = list(map(int, input().split()))
price.insert(0,0)
memo = [-1 for _ in range(N+1)]

def dp(n):
    if n==1:
        memo[n] = price[n]
    elif memo[n] == -1:
        max_ = 0
        for i in range(1,n):
            max_ = max(dp(i) + dp(n-i), max_) 
        memo[n] = max(max_, price[n])

    return memo[n]

dp(N)
print(memo[N])