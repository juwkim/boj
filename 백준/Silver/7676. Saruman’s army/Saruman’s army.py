import sys
g = lambda: map(int, sys.stdin.readline().split())

while True:
    R, n = g()
    if R == -1:
        break
    xs = sorted(g())
    ans, covered, i = 0, -1e9, 0
    while i < n:
        if xs[i] > covered:
            ans += 1
            cur = i
            while i + 1 < n and xs[i + 1] - xs[cur] <= R:
                i += 1
            covered = xs[i] + R
        i += 1
    print(ans)