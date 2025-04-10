import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l = []
    for s in input().split():
        a, b = map(int, s.split('.'))
        l.append(a * 100 + b)
    R, B, M = l
    i = 0
    while B > 0 and i < 1200:
        B += (B * R + 5000) // 10000 - M
        i += 1
    if B > 0:
        print("impossible")
    else:
        print(i)