g = lambda: map(int, input().split())

input()
ans, cum = 0, 0
for s, t in sorted((si, ti) for ti, si in zip(g(), g()) if si != -1):
    cum += t
    ans = max(ans, (cum + s - 1) // s)
print(ans)