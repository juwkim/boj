import sys
input = sys.stdin.readline
from math import lcm

for _ in range(int(input())):
    a, b, S = map(int, input().split())
    ans = 1e9, 1e9
    l = lcm(a, b)
    for i in range(min(l // a, S // a + 1)):
        j, r = divmod(S - i * a, b)
        if r == 0 and i + j < sum(ans):
            ans = i, j
    for i in range(min(l // b, S // b + 1)):
        j, r = divmod(S - i * b, a)
        if r == 0 and i + j < sum(ans):
            ans = j, i
    print("Impossible") if ans[0] == 1e9 else print(*ans)