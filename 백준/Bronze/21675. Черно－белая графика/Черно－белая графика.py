g = lambda: [*map(int, input().split())]

w, h = g()
a = [input() for _ in range(h)]
b = [input() for _ in range(h)]
s = input()
for i in range(h):
    tmp = [s[2 * int(x) + int(y)] for x, y in zip(a[i], b[i])]
    print(*tmp, sep='')