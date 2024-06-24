import sys
N = sys.stdin.readline().strip()
length = 0
for i in range(1, len(N)): 
    length += (9 * 10**(i-1)) * i # N이 3자리 수라면 2자리 수까지 이어붙인 길이를 구함

length += (int(N) - 10**(len(N)-1) + 1) * len(N)
print(length)
