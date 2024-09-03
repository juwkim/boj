import sys
input = sys.stdin.readline

A, B, C, D = float('inf'), float('inf'), -float('inf'), -float('inf')
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    A, B, C, D = min(A, a), min(B, b), max(C, c), max(D, d)
    print(2 * (C - A + D - B))