import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
D = int(input())
P = D - (N // 2 + M // 2)
ans = 0
for i in range(N):
    s = N // 2
    if N % 2 == 0 and i < N // 2:
        s -= 1
    for j in range(M):
        t = M // 2
        if M % 2 == 0 and j < M // 2:
            t -= 1
        if abs(i - s) + abs(j - t) < P:
            ans += 1
print(ans)