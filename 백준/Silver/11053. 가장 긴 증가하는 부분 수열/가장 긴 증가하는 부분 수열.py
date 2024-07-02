n = int(input())
lst = list(map(int, input().split()))
memo = [1] * n

for i in range(n):
    for j in range(0,i):
        if lst[j] < lst[i] :
            memo[i] = max(memo[j] + 1, memo[i])

print(max(memo))
    