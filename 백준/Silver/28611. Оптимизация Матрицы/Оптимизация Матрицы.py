n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
pref, suf = [0] * (n + 1), [0] * (n + 2)

for i in range(n):
    pref[i] = a[i] + pref[i - 1]

for i in range(n, 0, -1):
    suf[i] = suf[i + 1] + a[i]

ans = 0
for i in range(1, n + 1):
    cur_ans = pref[max(0, i - k - 1)] + suf[min(n + 1, i + k + 1)]
    cur_ans += a[i] * (1 + min(k, n - i) + min(k, i - 1))
    ans = max(ans, cur_ans)
print(ans)