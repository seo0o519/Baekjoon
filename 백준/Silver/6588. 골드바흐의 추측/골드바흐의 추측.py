import sys
input=sys.stdin.readline

max = 1000000
is_prime_num = [True] * (max+1)

for i in range(2, int((max+1)**(1/2))+1):
    if is_prime_num[i]:
        for j in range(i+i, max+1, i): 
            is_prime_num[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    
    for i in range(3, max//2, 2):
        if is_prime_num[i] and is_prime_num[n-i]:
            print (f'{n} = {i} + {n-i}')
            break