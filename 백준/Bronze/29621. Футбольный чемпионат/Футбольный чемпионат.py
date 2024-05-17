import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a, b = input(), input()
s, t = -1, -1
team = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if name == a:   s = -score
    elif name == b: t = -score
    else: team.append((-score, name))
print(*[
    1 + ((t, b) < (s - 3, a)) + sum(x < (s - 3, a) for x in team),
    1 + ((t - 1, b) < (s - 1, a)) + sum(x < (s - 1, a) for x in team),
    1 + ((t - 3, b) < (s, a)) + sum(x < (s, a) for x in team)
])