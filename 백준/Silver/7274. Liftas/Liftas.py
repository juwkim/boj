import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
ans = sum(sorted([int(input()) for _ in range(N)])[:N-K])
print(ans)