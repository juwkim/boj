from itertools import permutations

pos = [[] for _ in range(4)]
N = int(input())
s, e = None, None
for i in range(N):
    for j, c in enumerate(input()):
        if c == 'H':
            s = i, j
        elif c == '#':
            e = i, j
        elif c != 'X':
            pos["JCBW".index(c)].append((i, j))
ans = 1e9, 0
for i in range(4):
    for p in permutations(pos[i]):
        p = [s] + list(p) + [e]
        dist = sum(abs(p[i][0] - p[i + 1][0]) + abs(p[i][1] - p[i + 1][1]) for i in range(4))
        ans = min(ans, (dist, i))
print(("Assassin", "Healer", "Mage", "Tanker")[ans[1]])