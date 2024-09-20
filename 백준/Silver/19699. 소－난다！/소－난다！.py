from itertools import combinations

def seive(n):
    p = [0] * 2 + [1] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = 0
    return p

N, M, *H = map(int, open(0).read().split())
p = seive(1000 * M)
ans = sorted({num for num in map(sum, combinations(H, M)) if p[num]})
if ans:
    print(*ans)
else:
    print(-1)