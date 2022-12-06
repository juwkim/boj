from math import perm
S, P = list(input()), list(input())
try:
    for i in P:
        S.remove(i)
    ans = sum(perm(len(S), k) * (k + 1) for k in range(0, 1 + len(S)))
except:
    ans = 0
print(ans)