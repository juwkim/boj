import sys
input = sys.stdin.readline

r = 0
for _ in range(int(input())):
    a, b, p = map(int, input().split())
    r = max(r, (a * p + b * r + (a + b) // 2) // (a + b))
print(r)