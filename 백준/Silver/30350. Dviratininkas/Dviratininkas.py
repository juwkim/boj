import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
for i, num in sorted(enumerate([int(input()) for _ in range(N)], 1), reverse=True, key=lambda x: x[1])[:K]:
    print(i)