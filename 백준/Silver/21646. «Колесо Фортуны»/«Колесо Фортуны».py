n, *vals, a, b, k = map(int, open(0).read().split())
L = (a - 1) // k
R = (b - 1) // k
seen = bytearray(n)
for t in range(L, min(L + n, R + 1)):
    idx = t % n
    seen[idx] = True
    seen[-idx] = True
print(max(vals[i] for i in range(n) if seen[i]))