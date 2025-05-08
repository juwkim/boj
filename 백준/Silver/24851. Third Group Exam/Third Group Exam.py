g = lambda: map(int, input().split())

n, a, b = g()
ans = [''] * n
cnt = [0, 0]
tot = 0
for i, (x, y) in sorted([(i, p) for i, p in enumerate(zip(g(), g()))], key=lambda x: -abs(x[1][0] - x[1][1])):
    j = n - cnt[0] == a or (n - cnt[1] != b and x > y)
    ans[i] = 'PT'[j]
    cnt[j] += 1
    tot += (y, x)[j]
print(tot)
print(*ans)