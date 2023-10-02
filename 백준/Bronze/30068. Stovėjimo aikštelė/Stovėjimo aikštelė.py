import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dic = {}
for _ in range(int(input())):
    T, N = g()
    if N in dic:
        print(N, T - dic[N])
    else:
        dic[N] = T