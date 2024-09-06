import sys
input=sys.stdin.readline

n = int(input())
skill = [list(map(int, input().split())) for _ in range(n)]

team_start = []

min_gap = 10000000


def rec(start):
    global min_gap
    if len(team_start) == n//2:
        team_link = []
        # 링크 팀의 팀원 구하기
        for i in range(n):
            if i not in team_start:
                team_link.append(i)
    
        # 스타트 팀의 능력치 구하기
        start = 0
        for i in team_start:
            for j in team_start:
                if i!=j:
                    start += skill[i][j]

        # 링크 팀의 능력치 구하기
        link = 0
        for i in team_link:
            for j in team_link:
                if i!=j:
                    link += skill[i][j]

        if abs(start-link) < min_gap: min_gap = abs(start-link)


    for i in range(n):
        if start < i:
            if i not in team_start:
                team_start.append(i)
                rec(i)
                team_start.pop()
        

rec(0)
print(min_gap)