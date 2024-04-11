import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N, K = g()
    ans, prev = 0, -1e9
    for s, e in sorted(g() for _ in range(N)):
        prev = max(prev, s)
        if prev >= e:
            continue
        cnt = (e - prev + K - 1) // K
        ans += cnt
        prev += cnt * K
    print(f"Case #{tc}: {ans}")