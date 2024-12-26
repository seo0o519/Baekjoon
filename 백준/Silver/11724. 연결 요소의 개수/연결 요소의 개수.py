import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[False for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
visited = [False for _ in range(N+1)]
ans = 0 

def dfs(n):
    visited[n] = True
    for i in range(1,N+1):
        if graph[n][i] and not visited[i]:
            dfs(i)
    return 1

if M == 0 :
    print(N)
else:
    for i in range(1,N+1):
        if not visited[i]:
            ans += dfs(i)
    print(ans)
