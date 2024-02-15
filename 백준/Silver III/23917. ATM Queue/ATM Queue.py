import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N, X = g()
    A = g()
    ans = sorted(range(1, N + 1), key=lambda i: ((A[i - 1] + X - 1) // X, i))
    print(f"Case #{tc}:", *ans)