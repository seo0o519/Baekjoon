N = int(input())
memo = [0]*(N+1)

def rec(n):
    # base case
    if n==1 :
        memo[n] = 1
        return memo[n]
    elif n==2 :
        memo[n] = 3
        return memo[n]
    
    # 이전에 계산된 값이 있는 경우
    elif memo[n] != 0 :
        return memo[n] 
    else:
        memo[n] = rec(n-1) + rec(n-2) * 2 
        return memo[n]

print(rec(N)%10007)