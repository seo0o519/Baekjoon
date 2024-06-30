N = int(input())
memorization = [0]*(N+1) # 저장 공간 초기화
def fibo(n):
    if memorization[n]!=0: # 값이 이미 저장된 경우
        return memorization[n]
    else:
        if n < 2: # n이 0 또는 1일 때
            memorization[n] = n
        else:
            memorization[n] = fibo(n-1) + fibo(n-2)

        return memorization[n]
    
print(fibo(N))
