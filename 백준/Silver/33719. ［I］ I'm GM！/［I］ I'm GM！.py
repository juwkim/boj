import sys
input = sys.stdin.readline

N = int(input())
r = 0
for _ in range(N):
    a, b, p = map(int, input().split())
    r = max(r, (a * p + b * r + (a + b) // 2) // (a + b))
print(r)