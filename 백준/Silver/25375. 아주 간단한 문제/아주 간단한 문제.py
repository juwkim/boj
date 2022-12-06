import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    a, b = g()
    r, q = divmod(b, a)
    if r > 1 and q == 0:
        print(1)
    else:
        print(0)