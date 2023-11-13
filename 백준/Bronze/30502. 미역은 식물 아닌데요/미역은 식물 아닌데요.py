import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
Max = [[1, 0] for _ in range(N)]
Min = [[0, 1] for _ in range(N)]
for _ in range(M):
    a, b, c = input().split()
    a, c = int(a), int(c)
    Max[a - 1][b == 'M'] = c
    Min[a - 1][b == 'M'] = c
print(Min.count([1, 0]), Max.count([1, 0]))