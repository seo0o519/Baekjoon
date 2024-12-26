import sys
input=sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[False for _ in range(N+1)] for _ in range(N+1)] 

dfs_visited = [False for _ in range(N+1)]
bfs_visited = [False for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(n):
    dfs_visited[n] = True
    print(n, end=" ")
    for i in range(1,N+1):
        if not dfs_visited[i] and graph[n][i]:
            dfs(i)

def bfs(n):
    queue = deque([n])
    bfs_visited[n] = True

    while queue:
        q = queue.popleft()
        print(q, end=" ")
        for i in range(1,N+1):
            if not bfs_visited[i] and graph[q][i]:
                bfs_visited[i] = True
                queue.append(i)

dfs(V)
print()
bfs(V)
