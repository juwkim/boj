import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

n, m, k = g()
if k > min(n, m):
    print('Impossible')
else:
    print('Possible')
    s = '.' * m
    for _ in range(n-k):
        print(s)
    for i in range(k):
        print('.' * i + '*' + '.' * (m - i - 1))