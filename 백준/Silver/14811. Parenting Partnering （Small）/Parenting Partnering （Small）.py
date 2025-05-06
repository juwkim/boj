import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for tc in range(1, int(input()) + 1):
    AC, AJ = g()
    activity = [(0, 0, -1)] + sorted([(*g(), 0) for _ in range(AC)] + [(*g(), 1) for _ in range(AJ)]) + [(1440, 1440, -1)]
    dp = [[[1e9] * 721 for _ in range(2)] for _ in range(len(activity))]
    dp[0][0][0] = 0
    dp[0][1][0] = 0
    for i in range(len(activity) - 1):
        for st in range(2):
            c0, d0, p0 = activity[i]
            c1, d1, p1 = activity[i + 1]
            if p0 == -1: p0 = st
            if p1 == -1: p1 = st
            task = (0, d1 - c1)[p1]
            for t in range(721):
                for gap in range(c1 - d0 + 1):
                    nt = t + gap + task
                    if nt > 720:
                        continue
                    if dp[i][st][t] == 1e9:
                        continue
                    if p0 != p1:
                        exch = 1
                    elif p0 == 1:
                        exch = 0 if gap == c1 - d0 else 2
                    else:
                        exch = 0 if gap == 0 else 2
                    dp[i + 1][st][nt] = min(dp[i + 1][st][nt], dp[i][st][t] + exch)
    print(f"Case #{tc}: {min(dp[-1][0][720], dp[-1][1][720])}")