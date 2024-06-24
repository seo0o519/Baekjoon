import sys
people = int(sys.stdin.readline())
friend_data = [sys.stdin.readline().strip() for i in range(people)]
ans = [0]*people
friend_list = [[] for i in range(people)]

for i in range(people):
    for j in range(people):
        if i==j:
            pass
        else:
            if friend_data[i][j]=="Y":
                if (j not in friend_list[i]):
                    friend_list[i].append(j)
                    ans[i] += 1
                for k in range(people):
                    if i!=k and friend_data[j][k]=="Y" and (k not in friend_list[i]):
                        friend_list[i].append(k)
                        ans[i] += 1
print(max(ans))
