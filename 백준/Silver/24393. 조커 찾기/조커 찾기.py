import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

cur = 1
for _ in range(int(input())):
    l, r = 0, 0
    for i, A in enumerate(g()):
        if i & 1:
            l += A
            if cur <= 13 and l >= cur:
                cur += r
                break
        else:
            r += A
            if cur > 13 and r >= cur - 13:
                cur += l - 13
                break
print(cur)