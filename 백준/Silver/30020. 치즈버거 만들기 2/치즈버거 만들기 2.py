import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

A, B = g()
K = A - B
if K <= 0 or K > B:
    print("NO")
else:
    print("YES")
    print(K)
    q, r = divmod(B, K)
    for _ in range(K - r):
        print("ab" * q + "a")
    for _ in range(r):
        print("ab" * (q + 1) + "a")