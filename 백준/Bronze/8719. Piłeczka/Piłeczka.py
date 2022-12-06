import sys
for _ in range(int(input())):
    x, w = map(int, sys.stdin.readline().split())
    t = 0
    while x * 2**t < w:
        t += 1
    print(t)