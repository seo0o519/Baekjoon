n = int(input())
memo = {1:0}
def dp(n):
    if n in memo.keys():
        return memo[n]
    if (n%3==0) and (n%2==0):
        memo[n] = min(dp(n//3)+1, dp(n//2)+1)
    elif n%3==0:
        memo[n] = min(dp(n//3)+1, dp(n-1)+1)
    elif n%2==0:
        memo[n] = min(dp(n//2)+1, dp(n-1)+1)
    else:
        memo[n] = dp(n-1)+1
    return memo[n]
print(dp(n))