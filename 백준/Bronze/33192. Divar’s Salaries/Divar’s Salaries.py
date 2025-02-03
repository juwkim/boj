import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, k, h = map(int, input().split())
    ans = x * (h * 4 + max(0, k - h - 140) * 3 + min(140, k - h) * 2) >> 1
    print(f"{ans:,}")