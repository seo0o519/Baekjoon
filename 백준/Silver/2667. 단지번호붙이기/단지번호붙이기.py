import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [input() for _ in range(N)]
visit = [[False] * N for _ in range(N)]
complex = []

def dfs(n, m):
    if visit[n][m] or graph[n][m] == "0":
        visit[n][m] = True
        return 0
     
    elif graph[n][m] == "1" and not visit[n][m]:
        visit[n][m] = True
        if  0 < n < N-1 and 0 < m < N-1:
            return 1 + dfs(n-1, m) + dfs(n+1, m) + dfs(n, m-1) + dfs(n, m+1)
        elif 0 < n < N-1 and m == 0:
            return 1 + dfs(n-1, m) + dfs(n+1, m) + dfs(n, m+1)
        elif 0 < n < N-1 and m == N-1:
            return 1 + dfs(n-1, m) + dfs(n+1, m) + dfs(n, m-1)
        elif 0 < m < N-1 and n == 0:
            return 1 + dfs(n+1, m) + dfs(n, m-1) + dfs(n, m+1)
        elif 0 < m < N-1 and n == N-1:
            return 1 + dfs(n-1, m) + dfs(n, m-1) + dfs(n, m+1)
        elif n == 0 and m == 0:
            return 1 + dfs(n+1, m) + dfs(n, m+1)
        elif n == 0 and m == N-1:
            return 1 + dfs(n+1, m) + dfs(n, m-1)
        elif n == N-1 and m == 0:
            return 1 + dfs(n-1, m) + dfs(n, m+1)
        elif n == N-1 and m == N-1:
            return 1 + dfs(n-1, m) + dfs(n, m-1)
    
    return 0


for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            result = dfs(i,j)
            if result != 0:
                complex.append(result)

complex.sort()
print(len(complex))
[print(complex[i]) for i in range(len(complex))]
