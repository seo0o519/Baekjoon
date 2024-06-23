import sys
teacher = []
for i in range(3):
    teacher.append(sys.stdin.readline().strip()) # 입력 각도 저장

if teacher[1]=="+":
    print(int(teacher[0])+int(teacher[2]))
else:
    print(int(teacher[0])*int(teacher[2]))