import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

M, H = g()
ans = 0
for _ in range(int(input())):
    C, B = g()
    ans += max(M * C, H * B)
print(ans)