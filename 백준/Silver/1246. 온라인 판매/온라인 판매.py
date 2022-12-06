g = lambda: [*map(int, input().split())]

N, M = g()
P = [int(input()) for _ in range(M)]
P.sort(reverse=True)

total = 0
cost = 0
for i in range(min(N, M)):
    if P[i] * (i + 1) >= total:
        total = P[i] * (i + 1)
        cost = P[i]
print(cost, total)