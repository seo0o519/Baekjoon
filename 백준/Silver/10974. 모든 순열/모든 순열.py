N = int(input())
lst = []

def rec(lst):
    if len(lst) == N :
        print(" ".join(map(str, lst)))
        return
    
    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            rec(lst)
            lst.pop()

rec([])