a, b, k = map(int, input().split())
cnt = 2 * (a // k + b // k)
s, t = a % k, b % k
if s + t == 0:
    pass
elif 2 * (s + t) <= k:
    cnt += 1
elif s + t <= k or 2 * max(s, t) <= k:
    cnt += 2
elif 2 * min(s, t) > k:
    cnt += 4
else:
    cnt += 3
print(cnt)