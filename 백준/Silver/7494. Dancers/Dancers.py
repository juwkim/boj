import sys
input = sys.stdin.readline

N = int(input())
coords = [[*map(int, input().split())] for _ in range(N)]
used = bytearray(N)
pairs = []
for _ in range(N >> 1):
    cur = 1e18, None
    for i in range(N):
        if used[i]: continue
        for j in range(i + 1, N):
            if used[j]: continue
            dist2 = (coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2
            cur = min(cur, (dist2, (i, j)))
    i, j = cur[1]
    used[i], used[j] = True, True
    pairs.append((i + 1, j + 1))

for a, b in sorted(pairs):
    print(a, b)