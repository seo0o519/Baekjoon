import sys
input=sys.stdin.readline

N = int(input())
deque = []
for _ in range(N):
    lst = list(input().split())

    if lst[0] == "push_front":
        deque.insert(0,lst[1])
    
    elif lst[0] == "push_back":
        deque.append(lst[1])

    elif lst[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))

    elif lst[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())

    elif lst[0] == "size":
        print(len(deque))

    elif lst[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif lst[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif lst[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])