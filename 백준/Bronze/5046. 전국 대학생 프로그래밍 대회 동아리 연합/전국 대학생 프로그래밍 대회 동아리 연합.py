g = lambda: [*map(int, input().split())]
f = lambda: int(input())

N, B, H, W = g()
ans = 500001
for _ in range(H):
    p = f()
    num = max(g())
    if num >= N and p * N <= B:
        ans = min(ans, p * N)
print(ans if ans != 500001 else 'stay home')