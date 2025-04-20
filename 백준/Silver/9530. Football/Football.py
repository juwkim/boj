import sys
g = lambda: map(int, sys.stdin.readline().split())

N, G = g()
draws, losses = 0, []
ans = 0
for _ in range(N):
    S, R = g()
    if S > R:
        ans += 3
    elif S == R:
        ans += 1
        draws += 1
    else:
        losses.append(R - S)

k = min(draws, G)
ans += 2 * k
G -= k
if G:
    for d in sorted(losses):
        if G < d:
            break
        if G == d:
            ans += 1
            break
        ans += 3
        G -= d + 1
print(ans)