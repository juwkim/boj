g = lambda: [*map(int, input().split())]

N, M = g()
six, one = 1000, 1000
for _ in range(M):
    a, b = g()
    six = min(six, a)
    one = min(one, b)
if six >= one * 6:
    print(one * N)
else:
    r, q = divmod(N, 6)
    print(min(r * six + q * one, (r+1) * six))