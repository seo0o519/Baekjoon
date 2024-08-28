import sys
input=sys.stdin.readline

k = int(input())
lst = list(input().split())

ans1 = []

def dfs1(idx):
    if len(ans1) == k+1:
        print((''.join(ans1)))
        return
    
    for i in range(9, 9-k-1, -1):
        if f'{i}' not in ans1:
            if len(ans1) == 0:
                ans1.append(f'{i}')
                dfs1(idx+1)
            else:
                if lst[idx] == '<':
                    if int(ans1[-1]) < i:
                        ans1.append(f'{i}')
                        dfs1(idx+1)
                    else:
                        ans1.pop()
                        break
                elif lst[idx] == '>':
                    if int(ans1[-1]) > i:
                        ans1.append(f'{i}')
                        dfs1(idx+1)
                    else:
                        ans1.pop()
                        break

dfs1(-1)


ans2 = []

def dfs2(idx):
    if len(ans2) == k+1:
        print((''.join(ans2)))
        return
    
    for i in range(k+1):
        if f'{i}' not in ans2:
            if len(ans2) == 0:
                ans2.append(f'{i}')
                dfs2(idx+1)
            else:
                if lst[idx] == '<':
                    if int(ans2[-1]) < i:
                        ans2.append(f'{i}')
                        dfs2(idx+1)
                    else:
                        ans2.pop()
                        break
                elif lst[idx] == '>':
                    if int(ans2[-1]) > i:
                        ans2.append(f'{i}')
                        dfs2(idx+1)
                    else:
                        ans2.pop()
                        break

dfs2(-1)