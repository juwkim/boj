g = lambda: [*map(int, input().split())]

M, N = g()
buf = [input() for _ in range(M)]
ans = 0
for _ in range(N):
    s = input()
    ans += any(s in line for line in buf)
print(ans)