n, k = map(int, input().split())
buf = []
for _ in range(n):
    x, y, z = map(float, input().split())
    buf.append(x * x + y * y + z * z)
buf.sort()
ans = buf[k - 1] ** .5
print(ans)