import sys
input=sys.stdin.readline

n, m = map(int, input().split())

s = []

def dfs(start):
    if len(s)==m:
        # s의 모든 요소를 문자열로 변환 후, 요소들 사이에 ' '를 넣어서 문자열 하나로 합침
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1): # start~n까지의 자연수중에서 중복 없이 숫자를 고름
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)

