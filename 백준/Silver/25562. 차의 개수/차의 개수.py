import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
print(N * (N - 1) // 2)
cur = 1
for i in range(N):
    print(cur, end=' ')
    cur <<= 1
print()
print(N - 1)
print(*range(1, N + 1))