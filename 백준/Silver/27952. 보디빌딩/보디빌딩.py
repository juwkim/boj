g = lambda: [*map(int, input().split())]

N, X = g()

cur = 0
A, B = g(), g()
for a, b in zip(A, B):
    cur += b
    if cur < a:
        cur = -1
        break
if cur == -1:
    print(-1)
else:
    print((cur - A[-1]) // X)