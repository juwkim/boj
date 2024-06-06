g = lambda: [*map(int, input().split())]

N = int(input())
idxA = [[] for _ in range(101)]
for i, num in enumerate(g()):
    idxA[num].append(i)
M = int(input())
idxB = [[] for _ in range(101)]
for i, num in enumerate(g()):
    idxB[num].append(i)


ans = []
A, B = 0, 0
for i in range(100, 0, -1):
    P = [idx for idx in idxA[i] if idx >= A]
    Q = [idx for idx in idxB[i] if idx >= B]
    if P and Q:
        cnt = min(len(P), len(Q))
        ans.extend([i] * cnt)
        A, B = P[cnt - 1] + 1, Q[cnt - 1] + 1
print(len(ans))
print(*ans)