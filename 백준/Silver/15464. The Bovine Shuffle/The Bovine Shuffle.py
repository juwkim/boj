g = lambda: [*map(int, input().split())]

N = int(input())
a = g()
cows = g()
res = [0] * N
for j in range(3):
    for i in range(N):
        res[i] = cows[a[i]-1]
    cows = res.copy()

print(*res)