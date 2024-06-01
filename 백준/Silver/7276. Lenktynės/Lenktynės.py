import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
pos = [0] * (N + 1)
for i, car in enumerate(g()):
    pos[car] = i
bad = 0
for i in range(1, int(input()) + 1):
    a, b = g()
    if pos[a] == pos[b] + 1:
        pos[a], pos[b] = pos[b], pos[a]
    else:
        bad = i
        break
if bad:
    print("NE")
    print(bad)
else:
    print("TAIP")
    _, ans = zip(*sorted(((pos[i], i) for i in range(1, N + 1))))
    print(*ans)