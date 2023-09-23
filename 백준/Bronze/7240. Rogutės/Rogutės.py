import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, S = g()
cur = 0
for _ in range(N - 1):
    cur += int(input())
    if cur > S:
        cur -= 1
cur += int(input())
print(cur)