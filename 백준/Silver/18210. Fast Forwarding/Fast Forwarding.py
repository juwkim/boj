t = int(input()) + 1
ans, v = -1, 1
while t:
    cnt = t % (3 * v) // v
    a = (3, 1, 2, 4)[cnt + 2 * (cnt == 1) * (t > v)]
    ans += a
    t -= a * v
    v *= 3
print(ans)