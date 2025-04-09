import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    i = int((2 * (N - 1) / K + .25)**.5 - .5)
    x = N - 1 - (i * (i + 1) // 2 + (i + 1) // 2) * K
    if i & 1:
        x = -x
    print(x, "RL"[i & 1])