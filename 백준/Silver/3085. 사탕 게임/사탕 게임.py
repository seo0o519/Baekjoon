import sys
input=sys.stdin.readline

n = int(input())

board = [list(input()) for _ in range(n)]

ans = 0

# 가로로 교체
for i in range(n):
    for j in range(n-1):
        # 사탕 색깔이 다르면 위치 교체
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

            # 위치 교체 후 가장 긴 연속 부분 길이 계산
            # 가로
            for k in range(n):
                cnt = 1
                for l in range(1,n):
                    if board[k][l] == board[k][l-1]:
                        cnt += 1
                        if cnt > ans : ans = cnt
                    else:
                        cnt = 1
            # 세로
            for k in range(n):
                cnt = 1
                for l in range(1,n):
                    if board[l][k] == board[l-1][k]:
                        cnt += 1
                        if cnt > ans : ans = cnt
                    else:
                        cnt = 1
            # 교체한 사탕 원위치
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

# 세로로 교체
for i in range(n):
    for j in range(n-1):
        # 사탕 색깔이 다르면 위치 교체
        if board[j][i] != board[j+1][i]:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            # 위치 교체 후 가장 긴 연속 부분 길이 계산
            # 가로
            for k in range(n):
                cnt = 1
                for l in range(1,n):
                    if board[k][l] == board[k][l-1]:
                        cnt += 1
                        if cnt > ans : ans = cnt
                    else:
                        cnt = 1
            # 세로
            for k in range(n):
                cnt = 1
                for l in range(1,n):
                    if board[l][k] == board[l-1][k]:
                        cnt += 1
                        if cnt > ans : ans = cnt
                    else:
                        cnt = 1
            # 교체한 사탕 원위치
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(ans)