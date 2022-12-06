g = lambda: [*map(int, input().split())]
N, K, A = g()
p = K // A
buf = []
for _ in range(N):
    t, s = g()
    val = p // t * (t + s) + p % t
    if p % t == 0:
        val -= s
    buf.append(val)
print(min(buf))