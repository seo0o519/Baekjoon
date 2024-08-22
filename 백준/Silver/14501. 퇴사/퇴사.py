import sys
input=sys.stdin.readline

n = int(input())

t_p = [list(map(int, input().split())) for _ in range(n)]
t_p.insert(0, [0,0]) # 인덱스랑 날짜 일치시키기 위함
max_price = [0 for _ in range(n+1)]
[0,0,0,10,30,30,45,45]

for i in range(1, n+1):
    max_price[i] = max(max_price[i-1], max_price[i])
    fin_date = i + t_p[i][0] -1
    if fin_date < n+1 :
        max_price[fin_date] = max(max_price[fin_date], max_price[i-1] + t_p[i][1])

print(max_price[n])
