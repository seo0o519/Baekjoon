import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = []
ans = 0 

def dfs(n): 
    visit.append(n) # 방문 노드 기록
    if len(visit) >= 5: # 방문 노드가 5개 이상이면 즉시 종료
        return True

    for i in graph[n]: # 현재 노드의 자식 노드 탐색
        if i not in visit: # 자식 노드와 간선 존재 & 미방문 노드면
            if dfs(i): # 그 자식노드 탐색
                return True # 연결된 총 노드가 5개 이상이면 즉시 종료
    visit.pop()
    return False

for i in range(N):
    result = dfs(i)
    if result == True:
        print(1)
        break
    elif result == False and i == N-1:
        print(0)