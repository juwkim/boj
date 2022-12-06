import sys
input = sys.stdin.readline
mod = 1_000_000_007
g = lambda: [*map(int, input().split())]

N, x = g()
val = int(input().split()[0])
for _ in range(N):
    p = int(input().split()[0])
    val = (val * x + p) % mod
print(val)