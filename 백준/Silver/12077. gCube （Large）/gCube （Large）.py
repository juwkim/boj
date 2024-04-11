from math import log, e
g = lambda: map(int, input().split())
for tc in range(1, 1 + int(input())):
    N, M = g()
    px = [0]
    for num in g(): px.append(px[-1] + log(num))
    print(f"Case #{tc}:")
    for _ in range(M):
        L, R = g()
        print(e ** ((px[R + 1] - px[L]) / (R - L + 1)))