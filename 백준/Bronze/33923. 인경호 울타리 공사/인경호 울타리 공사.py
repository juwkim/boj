N, M = map(int, input().split())
a = min(N, M)
if N != M:
    print((a-1)**2)
elif a & 1:
    print(max((a-2)**2 + 1, (a-1)**2 // 2))
else:
    print((a-2)**2 + 1)