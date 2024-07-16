import sys
input = sys.stdin.readline

for _ in range(int(input())):
    L, R, S = map(int, input().split())
    print(min(2 * (R - S), 2 * (S - L) + 1))