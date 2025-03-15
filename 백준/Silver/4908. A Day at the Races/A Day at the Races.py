import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, Counter

tc = 1
nums = 0, 10, 8, 6, 5, 4, 3, 2, 1
while N:=int(input()):
    res, team = defaultdict(lambda: [0] * 9), Counter()
    for _ in range(N):
        input(), input()
        for i in range(1, 9):
            _, first_name, last_name, *team_name = input()[:-1].split()
            res[(last_name, first_name)][0] -= nums[i]
            res[(last_name, first_name)][i] -= 1
            team[' '.join(team_name)] -= nums[i]
        input()
    print(f"Season {tc}:")
    print("Drivers Standing:")
    for k, v in sorted(res.items(), key=lambda x: (x[1], x[0])):
        print(f"{k[1] + ' ' + k[0]:<25} {-v[0]}")
    print()
    print("Teams Standing:")
    for k, v in sorted(team.items(), key=lambda x: (x[1], x[0])):
        print(f"{k:<25} {-v}")
    print()
    tc += 1