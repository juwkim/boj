import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    R, C, W = map(int, input().split())
    ans = C // W * (R - 1) + (C - 1) // W + W
    print(f"Case #{tc}: {ans}")