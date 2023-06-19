g = lambda: [*map(int, input().split())]

n, m, k = g()
buf = [g() for _ in range(k)]
ans = min(range(k), key=lambda x: buf[x][0] - buf[x][1]) + 1
print(ans)