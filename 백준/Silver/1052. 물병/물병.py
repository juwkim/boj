import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
ans = 0
while N.bit_count() > K:
    b = bin(N)[::-1]
    i1 = b.index("1")
    i2 = b.index("1", i1 + 1)
    num = 2 ** i2 - 2 ** i1
    ans += num
    N += num
print(ans)