import sys
input = sys.stdin.readline

N, M = map(int, input().split())
teams = []
skip = True
for _ in range(N + 1):
    team_name, *l = input().split()
    if team_name == "NijeZivotJedanACM" and skip:
        skip = False
        continue
    solved, penalty = 0, 0
    for problem in l:
        if problem[0] == '-': continue
        solved += 1
        attempts, time = problem[1:].split('/')
        h, m, s = map(int, time.split(":"))
        penalty += h * 3600 + m * 60 + s + (int(attempts) - 1) * 1200
    teams.append((-solved, penalty, team_name))

for rank, (_, _, team_name) in enumerate(sorted(teams), 1):
    if team_name == "NijeZivotJedanACM":
        print(rank)
        break