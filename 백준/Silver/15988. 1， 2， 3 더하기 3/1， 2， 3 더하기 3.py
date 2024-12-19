T = int(input())
num = [int(input()) for _ in range(T)]
memo = [0, 1, 2, 4]

for n in range(len(memo),max(num)+1):
    memo.append((memo[n-1] + memo[n-2] + memo[n-3])%1000000009)

for i in range(T):
    print(memo[num[i]])