import math
A = list(map(int, input().split()))
N = A[0]
M = A[1]
data = []
for i in range(M):
    data.append(list(map(int, input().split())))
min_6_cost = data[0][0]
min_1_cost = data[0][1]
for i in range(M):
    if min_6_cost > data[i][0]:
        min_6_cost = data[i][0]
    if min_1_cost > data[i][1]:
        min_1_cost = data[i][1]

ans = []
ans.append(min_1_cost * N)
ans.append(min_6_cost * math.ceil(N/6))
ans.append(min_6_cost * (N//6) + min_1_cost * (N%6))
print(min(ans))