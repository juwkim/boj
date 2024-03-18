import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    N, *l = g()
    PA, PB = sorted(l)
    a, b = 0, 0
    reserve, cnt = 0, 0
    for num in g():
        if num - PA == PB - num:
            reserve = num - PA
            cnt += 1
        elif num - PA > PB - num:
            b += PB - num
        else:
            a += num - PA
    for i in range(cnt):
        if a < b:
            a += reserve
        else:
            b += reserve
    a <<= 1
    b <<= 1
    print(a + b, abs(a - b))