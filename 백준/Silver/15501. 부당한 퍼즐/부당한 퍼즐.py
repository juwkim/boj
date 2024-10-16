import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
a = g()
b = g()
i = b.index(a[0])
if all(a[j] == b[i + j] for j in range(-n, 0)) or all(a[j] == b[i - j] for j in range(n)):
    print('good puzzle')
else:
    print('bad puzzle')