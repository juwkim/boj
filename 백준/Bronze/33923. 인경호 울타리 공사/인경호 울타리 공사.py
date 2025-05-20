N, M = map(int, input().split())
a = min(N, M)
if N == M:
    print((a-2)**2 + 1)
else:
    print((a-1)**2)