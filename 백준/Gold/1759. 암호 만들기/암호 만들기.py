import sys
input=sys.stdin.readline

l, c = map(int, input().split())
alphabets = list(input().split())
alphabets.sort()
ans = []

def recursion(start):
    if len(ans) == l:
        # 만약 모음이 1개 이상, 자음이 2개 이상이면 print해라
        # 아니면 그냥 return
        cnt = 0
        for a in ans:
            if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
                cnt += 1
        if (cnt >= 1) and (l-cnt >= 2):
            print(''.join(ans))
        
        return
    
    for i in alphabets:
        if i not in ans:
            if start < i :
                ans.append(i)
                recursion(i)
                ans.pop()

recursion("0")
