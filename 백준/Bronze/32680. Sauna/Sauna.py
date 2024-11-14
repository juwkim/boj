import sys
input = sys.stdin.readline

A, B = -1e6, 1e6
for _ in range(int(input())):
    a, b = map(int, input().split())
    A, B = max(A, a), min(B, b)
if A > B:
    print("bad news")
else:
    print(B - A + 1, A)