g = lambda: [*map(int, input().split())]

N, M = g()
score = g()
res = []
for _ in range(M):
    num, *l = input().split()
    num = int(num)
    get = sum((i == 'O') * j for i, j in zip(l, score))
    res.append((get, -num))
get, num = max(res)
print(-num, get)