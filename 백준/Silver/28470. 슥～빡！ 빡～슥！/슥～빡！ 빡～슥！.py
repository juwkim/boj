g = lambda: [*map(int, input().split())]

N = int(input())
A, B = g(), g()
K = []
for s in input().split():
    p, q = map(int, s.split('.'))
    K.append(p * 10 + q)

ans = 0
for A, B, K in zip(A, B, K):
    d = max(A * K // 10 - B, A - B * K // 10)
    ans += d
print(ans)