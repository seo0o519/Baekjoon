N = int(input())
lst = list(map(int, input().split()))
memo = [1] * N
idx = [n for n in range(N)]
ans = []

for i in range(N):
    for j in range(0,i):
        if lst[j] < lst[i] :
            if memo[j]+1 > memo[i]:
                idx[i] = j
                memo[i] = memo[j] + 1

start_index = memo.index(max(memo)) # 리스트의 최대값 요소의 인덱스 구하기
while True:
    ans.append(lst[start_index])
    if start_index == idx[start_index]:
        break
    start_index = idx[start_index]

ans = ans[::-1]

print(max(memo))
[print(i, end=" ") for i in ans]
