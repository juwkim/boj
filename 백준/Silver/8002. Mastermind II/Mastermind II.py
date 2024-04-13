import sys
input = sys.stdin.readline
from itertools import permutations

A, B, codes = [], [], []
c = int(input())
for _ in range(c):
    a, b, *code = map(int, input().split())
    A.append(a)
    B.append(b)
    codes.append(code)
for l in permutations(range(1, 10), c):
    for i in range(c):
        a = 0
        X, Y = bytearray(10), bytearray(10)
        for p, q in zip(l, codes[i]):
            if p == q:
                a += p
            else:
                X[p], Y[q] = True, True
        if a != A[i]:
            break
        b = sum(i for i in range(1, 10) if X[i] and Y[i])
        if b != B[i]:
            break
    else:
        print(*l)
        break