import sys
input = sys.stdin.readline

x = 0
for _ in range(int(input())):
    A, B, C, D = map(int, input().split())
    r = x % (C + D)
    x = min(x + B, x + A if r < C else x + A + C + D - r)
print(x)