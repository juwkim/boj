import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(-3 * x, 3 * y, -4 * x, 2 * y)