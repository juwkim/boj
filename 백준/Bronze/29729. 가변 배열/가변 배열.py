import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

S, N, M = g()
U = 0
for _ in range(N + M):
    if int(input()):
        if U == S:
            S <<= 1
        U += 1
    else:
        U -= 1
print(S)