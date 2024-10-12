from collections import Counter
from itertools import chain
g = lambda: [*map(int, input().split())]

r, c, k = g()
A = [g() for _ in range(3)]
rl, cl = 3, 3
time = 0
transpose = False
while time < 100:
    if r <= rl and c <= cl and A[r - 1][c - 1] == k:
        break
    if rl >= cl + transpose:
        cl = 0
        for i in range(rl):
            cnt = Counter(A[i])
            del cnt[0]
            A[i] = [*chain(*sorted(cnt.items(), key=lambda x: (x[1], x[0])))][:100]
            cl = max(cl, len(A[i]))
        for i in range(rl):
            A[i].extend([0] * (cl - len(A[i])))
        time += 1
    else:
        A = [*zip(*A)]
        rl, cl, r, c = cl, rl, c, r
        transpose ^= 1
print(time if r <= rl and c <= cl and A[r - 1][c - 1] == k else -1)