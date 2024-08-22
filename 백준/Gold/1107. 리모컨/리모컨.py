import sys
input=sys.stdin.readline

channel = int(input())
n = int(input())
if n:
    broken = list(map(int, input().split()))
    if len(broken)!=10:
        #channel에서 1씩 빼가며 조건을 만족하는 channel보다 작은 가장 큰 숫자를 찾는다.
        a = 500000
        for i in range(channel, -1, -1):
            digits = [int(digit) for digit in str(i)]
            if set(digits) & set(broken):
                continue
            else:
                a = i
                break

        #channel에서 1씩 더해가며 조건을 만족하는 channel보다 큰 가장 작은 숫자를 찾는다.
        b = 0
        for i in range(channel,999999):
            digits = [int(digit) for digit in str(i)]
            if set(digits) & set(broken):
                continue
            else:
                b = i
                break
        num = 0
        if abs(channel-a) > abs(channel-b):
            num = b
        else:
            num = a

        print(min(abs(channel-100), len(str(num))+abs(channel-num) ))
    else:
        print(abs(channel-100))
else:
    print(min(len(str(channel)), abs(channel-100)))
             