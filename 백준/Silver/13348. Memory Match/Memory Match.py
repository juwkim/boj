import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
revealed = set()
check = defaultdict(set)
for _ in range(int(input())):
    C1, C2, P1, P2 = input().split()
    revealed.add(P1)
    revealed.add(P2)
    if P1 == P2:
        if P1 in check:
            del check[P1]
        continue
    check[P1].add(C1)
    check[P2].add(C2)
if 2 * len(revealed) == N:
    ans = len(check)
else:
    ans, flag = 0, True
    for v in check.values():
        if len(v) == 1:
            flag = False
        else:
            ans += 1
    if flag and 2 * len(revealed) == N - 2:
        ans += 1
print(ans)