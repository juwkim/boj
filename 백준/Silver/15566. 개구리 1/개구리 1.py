import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import product

N, M = g()
preference = [g() for _ in range(N)]
frogs = [{*g()} for _ in range(N)]
logs = [g() for _ in range(M)]

ans = "NO"
for l in product(*frogs):
    if len(set(l)) != N:
        continue
    arr = [0] * (N + 1)
    for i, c in enumerate(l, 1):
        arr[c] = i
    for A, B, T in logs:
        frog1, frog2 = arr[A], arr[B]
        if preference[frog1 - 1][T - 1] != preference[frog2 - 1][T - 1]:
            break
    else:
        ans = "YES"
        break
print(ans)
if ans == "YES":
    print(*arr[1:])