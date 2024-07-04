import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
t_p = [list(map(int, input().split())) for _ in range(n)]
t_p.insert(0, [0,0]) # 인덱스랑 날짜 일치시키기 위함
memo = [0 for _ in range(n+1)]

for i in range(1,n+1):
    memo[i] = max(memo[i-1], memo[i])
    fin_date = i + t_p[i][0] - 1
    if fin_date < n+1 :
        memo[fin_date] = max(memo[fin_date], memo[i-1] + t_p[i][1])
print(memo[n])
