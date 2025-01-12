g = lambda: [*map(int, input().split())]

N, M = g()
A, B = g(), g()
ans = sum(max(a, b) * (a + b) for a in A for b in B)
print(ans)