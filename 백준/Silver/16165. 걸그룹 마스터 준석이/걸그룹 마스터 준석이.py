g = lambda: map(int, input().split())

from collections import defaultdict
N, M = g()
members = defaultdict(list)
teams = {}
for _ in range(N):
    team = input()
    for _ in range(int(input())):
        member = input()
        members[team].append(member)
        teams[member] = team
for team in members:
    members[team].sort()
for _ in range(M):
    s = input()
    if int(input()):
        print(teams[s])
    else:
        print(*members[s], sep='\n')