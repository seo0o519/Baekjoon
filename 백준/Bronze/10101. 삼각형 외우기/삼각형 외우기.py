import sys
angle = []
for i in range(3):
    angle.append(int(sys.stdin.readline().strip())) # 입력 각도 저장

if angle[0] == angle[1] == angle[2] == 60:
    ans = "Equilateral"
elif angle[0] + angle[1] + angle[2] == 180:
    if angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]:
        ans = "Isosceles"
    else:
        ans = "Scalene"
else:
    ans = "Error"

print(ans)