import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(lambda: [0, 0, 0, 0, 0, 0])
    for _ in range(int(input())):
        team1, score1, _, score2, team2 = input().split()
        score1, score2 = int(score1[1:]), int(score2[:-1])
        if score1 > score2:
            d[team1][0] += 3
            d[team1][1] += 1
            d[team2][3] += 1
        elif score1 < score2:
            d[team2][0] += 3
            d[team2][1] += 1
            d[team1][3] += 1
        else:
            d[team1][0] += 1
            d[team1][2] += 1
            d[team2][0] += 1
            d[team2][2] += 1
        d[team1][4] += score1
        d[team1][5] += score2
        d[team2][4] += score2
        d[team2][5] += score1
    for k in sorted(d, key=lambda x: (-d[x][0], -d[x][1], -d[x][2], d[x][3], -d[x][4], d[x][5])):
        print(k, *d[k], sep=',')
    print()