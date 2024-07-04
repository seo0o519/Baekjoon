import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
memo = [-1 for _ in range(k+1)]
memo[0] = 0

def rec(n):
    if n < 0 :
        return k
    if memo[n] == -1 :
        memo[n] = min(rec(n-c) for c in coin) + 1
    return memo[n]

ans =  rec(k) 
if ans > k :
    print(-1)
else :
    print(ans)
