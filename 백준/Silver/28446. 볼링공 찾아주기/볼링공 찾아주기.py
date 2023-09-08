import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dic = {}
for _ in range(int(input())):
    n, *x, w = g()
    if n == 1:
        dic[w] = x[0]
    else:
        print(dic[w])