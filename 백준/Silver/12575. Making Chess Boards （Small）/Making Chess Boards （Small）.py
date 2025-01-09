import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

for tc in range(1, 1 + int(input())):
    M, N = map(int, input().split())
    a = []
    for _ in range(M):
        b = []
        for c in map(lambda x: int(x, 16), input()):
            b.extend(c >> i & 1 for i in (3, 2, 1, 0))
        a.append(b)
    visited = [bytearray(N) for _ in range(M)]
    cnt = Counter()
    for l in range(min(M, N), 0, -1):
        for i in range(M - l + 1):
            for j in range(N - l + 1):
                if all(a[i + x][j + y] == (a[i][j] ^ x ^ y) & 1 and not visited[i + x][j + y] for x in range(l) for y in range(l)):
                    cnt[l] += 1
                    for s in range(i, i + l):
                        for t in range(j, j + l):
                            visited[s][t] = 1
    print(f"Case #{tc}: {len(cnt)}")
    for s, t in sorted(cnt.items(), reverse=True):
        print(s, t)