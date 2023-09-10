import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

A, B = g()
K, X = g()

ans = 0
for i in range(A, B + 1):
    ans += abs(i - K) <= X
if ans == 0:
    print("IMPOSSIBLE")
else:
    print(ans)