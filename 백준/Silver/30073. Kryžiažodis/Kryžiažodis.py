import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve(A, B, C):
    for i in range(len(B)):
        s = A.find(B[i])
        if s == -1:
            continue
        for j in range(len(C)):
            if C[j] == B[i]:
                t = A.find(C[j], s + 1)
            else:
                t = A.find(C[j])
            if t == -1:
                continue
            print(A, s + 1, B, i + 1)
            print(A, t + 1, C, j + 1)
            exit()
p, q, r = input(), input(), input()
solve(p, q, r)
solve(q, p, r)
solve(r, p, q)