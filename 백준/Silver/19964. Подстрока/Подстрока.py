import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

s = input()
for _ in range(int(input())):
    l, r, t = input().split()
    if t in s[int(l) - 1:int(r)]:
        print("+", end="")
    else:
        print("-", end="")