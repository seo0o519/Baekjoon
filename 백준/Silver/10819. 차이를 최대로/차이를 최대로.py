N = int(input())
lst = list(map(int, input().split()))
ans = 0
swap = []
visited = []

def rec(swap):
    global ans # 전역 변수 ans를 수정할 수 있도록 선언
    global visited
    if len(swap) == N :
        tmp = 0
        for i in range(N-1):
            tmp += abs(swap[i] - swap[i+1])
        if tmp > ans : 
            ans = tmp
        return
    
    for i in range(N):
        if i not in visited:
            swap.append(lst[i])
            visited.append(i)
            rec(swap)
            swap.pop()
            visited.pop()

rec([])
print(ans)