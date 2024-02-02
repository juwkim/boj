import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N, M = map(int, input().split())
    t = N % M
    if t == 0:
        u = N - M
    else:
        u = N - t
    v = u - M
    if u <= 0 or v <= 0:
        print('Reseni neexistuje.')
    else:
        print(u, v)