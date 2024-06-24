import sys
N, M = map(int, sys.stdin.readline().split())
board = [0] * N
dice = [0] * M
for n in range(N):
    board[n] = int(sys.stdin.readline())
for m in range(M):
    dice[m] = int(sys.stdin.readline())

p = 0
loop = 0
while p < N-1 :
    p += dice[loop]
    loop += 1
    if p >= N-1 :
        break
    p += board[p]
print(loop)