N = int(input())
num = list(map(int, input().split()))

# 증가하는 부분 수열의 길이
dp_up = [1] * N
# 감소하는 부분 수열의 길이
dp_down = [1] * N

# 증가 부분 수열 계산 (왼쪽에서 오른쪽)
for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)

# 감소 부분 수열 계산 (오른쪽에서 왼쪽)
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if num[j] < num[i]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)

# 바이토닉 수열의 최대 길이 계산
max_length = 0
for i in range(N):
    max_length = max(max_length, dp_up[i] + dp_down[i] - 1)

print(max_length)