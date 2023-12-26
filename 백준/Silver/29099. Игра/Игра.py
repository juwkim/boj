import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
if (g()[-1] - n)&1:
    print("First")
else:
    print("Second")