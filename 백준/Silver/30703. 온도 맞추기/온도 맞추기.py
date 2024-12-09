import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

input()
ans, odd = 0, None
for A, B, X in zip(g(), g(), g()):
    q, r = divmod(abs(A - B), X)
    if r or odd is not None and q + odd & 1:
        ans = -1
        break
    ans, odd = max(ans, q), q & 1
print(ans)