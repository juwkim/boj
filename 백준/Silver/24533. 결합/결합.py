import sys
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
ans = 0
for _ in range(N - 1):
    c, d = map(int, input().split())
    ans += a * d + b * c
    a, b = a + c, b + d
print(ans)