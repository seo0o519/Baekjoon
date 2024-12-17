N = int(input())
perm = list(map(int, input().split()))

x = 0
y = 0

# 순열 맨 뒤에서부터 앞 < 뒤 가 되면 정지
for i in range(N-1, 0, -1):
    if perm[i-1] < perm[i]:
        x = i-1
        y = i
        # 순열 맨 뒤에서부터 x < 뒤 면 swap
        for j in range(N-1, 0, -1):
            if perm[x] < perm[j]:
                temp = perm[x]
                perm[x] = perm[j]
                perm[j] = temp
                break
        break
    else:
        continue

# y인덱스부터 끝까지 뒤집음
front = perm[0:x+1]
end = perm[y:][::-1]

if x==0 and y==0:
    print(-1)
else:
    for i in (front+end):
        if i==N-1 : print(i)
        else: print(i, end=" ")