import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import product

for tc in range(1, 1 + int(input())):
    C, J = input().split()
    idxc = [i for i in range(len(C)) if C[i] == '?']
    idxj = [i for i in range(len(J)) if J[i] == '?']
    ans = 0, 1000
    for c in product(range(10), repeat=len(idxc)):
        for j in product(range(10), repeat=len(idxj)):
            C_ = C
            J_ = J
            for i, v in zip(idxc, c):
                C_ = C_[:i] + str(v) + C_[i + 1:]
            for i, v in zip(idxj, j):
                J_ = J_[:i] + str(v) + J_[i + 1:]
            p = (int(C_), int(J_))
            q = (int(ans[0]), int(ans[1]))
            if abs(p[0] - p[1]) < abs(q[0] - q[1]) or abs(p[0] - p[1]) == abs(q[0] - q[1]) and p < q:
                ans = C_, J_
    print(f"Case #{tc}: {ans[0]} {ans[1]}")