import sys
N, Q = map(int, sys.stdin.readline().split())
res = [0]*(N+1)

for _ in [0]*Q:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        res[b] += c
    else:
        print(sum(res[b:c+1]))