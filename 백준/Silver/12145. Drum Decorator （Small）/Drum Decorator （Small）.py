import sys
from math import lcm
input = sys.stdin.readline

MOD = 10**9 + 7
for tc in range(1, 1 + int(input())):
    R, C = map(int, input().split())
    a, b = [[0] * 13 for _ in range(4)], [[0] * 13 for _ in range(4)]
    a[0][1], b[0][1] = 1, 1
    for i in range(R):
        for d, v in enumerate(a[i % 4]):
            if v == 0: continue
            if i + 2 <= R:
                b[(i + 2) % 4][d] += v
        for d, v in enumerate(b[i % 4]):
            if v == 0: continue
            if i + 1 <= R:
                a[(i + 1) % 4][d] += v
            if i + 2 <= R:
                if C % 3 == 0:
                    l = lcm(d, 3)
                    a[(i + 2) % 4][l] += 3 * v
                if C % 6 == 0:
                    l = lcm(d, 6)
                    a[(i + 2) % 4][l] += 6 * v
            if i + 3 <= R and C % 4 == 0:
                l = lcm(d, 4)
                a[(i + 3) % 4][l] += 4 * v
        a[i % 4], b[i % 4] = [0] * 13, [0] * 13
    ans = 0
    for d, v in enumerate(a[R % 4]):
        if v == 0: continue
        ans = (ans + v // d) % MOD
    for d, v in enumerate(b[R % 4]):
        if v == 0: continue
        ans = (ans + v // d) % MOD
    print(f"Case #{tc}: {ans}")