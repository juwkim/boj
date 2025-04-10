import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

M, N, Q = g()
a = g()
ans = [1] * N
for i in range(1, M + 1):
    print('?', i, i, flush=True)
    if int(input()) == 1:
        ans[i - 1] = 2
print('!', *ans, flush=True)