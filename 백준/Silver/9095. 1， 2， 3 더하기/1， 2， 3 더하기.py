for _ in range(int(input())):

    N = int(input())
    memo = [-1]*(N+1)

    def rec(n):
        # base case (1,2,3)
        if n <= 2 :
            memo[n] = n
        elif n==3 :
            memo[n] = 4
        
        # 처음 계산하는 값일 경우
        elif memo[n] < 0 :
            memo[n] = rec(n-1) + rec(n-2) + rec(n-3) 
        
        return memo[n]
    
    print(rec(N))
