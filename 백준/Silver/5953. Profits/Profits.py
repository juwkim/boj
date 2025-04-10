N, *P = map(int, open(0))
if all(p < 0 for p in P):
    ans = max(P)
else:
    ans, cur = 0, 0
    for p in P:
        cur = max(0, cur + p)
        ans = max(ans, cur)
print(ans)