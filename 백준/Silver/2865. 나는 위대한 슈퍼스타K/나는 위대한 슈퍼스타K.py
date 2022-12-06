g = lambda: [*map(int, input().split())]
N, M, K = g()
ans = [0] * (N + 1)
for _ in range(M):
    s = input().split()
    for i in range(0, len(s), 2):
        c = int(s[i])
        ans[c] = max(ans[c], float(s[i+1]))
print("%.1f" % sum(sorted(ans)[-K:]))