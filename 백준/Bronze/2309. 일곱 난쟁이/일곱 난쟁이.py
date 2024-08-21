import sys
input=sys.stdin.readline

dwarfs = [int(input()) for i in range(9)]
dwarfs.sort()
sum_ = sum(dwarfs)
not1 = 0
not2 = 0


for i in range(8):
    for j in range(i+1, 9):
        if sum_ - dwarfs[i] - dwarfs[j] == 100:
            not1 = i
            not2 = j
            break
    if not1: break

for i in range(9):
    if (i != not1) and (i != not2):
        print(dwarfs[i])
