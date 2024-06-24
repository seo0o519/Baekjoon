import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_sum = sum(num)
ans = 0
for idx,val in enumerate(num):
    num_sum -= num[idx]
    ans += num[idx] * num_sum
print(ans)