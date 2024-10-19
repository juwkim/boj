a, d, k = map(int, input().split())
d /= 100
k /= 100
ans, p, cnt = 0, 1, 1
while d < 1:
    ans += a * cnt * d * p
    p *= 1 - d
    d += d * k
    cnt += 1
ans += a * cnt * p
print(ans)