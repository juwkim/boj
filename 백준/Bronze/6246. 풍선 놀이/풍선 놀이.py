N, Q = map(int, input().split())
t = set()
for _ in range(Q):
    L, I = map(int, input().split())
    t |= {*range(L, N+1, I)}
print(N - len(t))