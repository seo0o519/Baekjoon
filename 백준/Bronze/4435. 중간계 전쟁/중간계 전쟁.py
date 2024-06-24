import sys
G_point = [1, 2, 3, 3, 4, 10]
S_point = [1, 2, 2, 2, 3, 5, 10]
for i in range(int(sys.stdin.readline())):
    G = list(map(int, sys.stdin.readline().split()))
    S = list(map(int, sys.stdin.readline().split()))
    for g in range(6):
        G[g] *= G_point[g]
    for s in range(7):
        S[s] *= S_point[s]

    if sum(G) > sum(S) :
        print(f"Battle {i+1}: Good triumphs over Evil")
    elif sum(G) < sum(S):
        print(f"Battle {i+1}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i+1}: No victor on this battle field")