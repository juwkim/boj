import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

input()
cur, *H = g()
for h, d in zip(H, g()):
    cur += d
    print("MVT"[(cur > h) - (cur < h)], end="")