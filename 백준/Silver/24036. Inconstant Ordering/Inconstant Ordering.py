import sys
input = sys.stdin.readline
from itertools import pairwise

a = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
for tc in range(1, 1 + int(input())):
    N = int(input())
    nums = [*map(int, input().split())]
    ans = ['A']
    for i, (L, NL) in enumerate(pairwise(nums)):
        if i & 1:
            ans.append(b[-L:])
        else:
            ans.append(a[:L - 1])
            ans.append(max(a[L - 1], b[-NL - 1]))
    L = nums[-1]
    if (N - 1) & 1:
        ans.append(b[-L:])
    else:
        ans.append(a[:L])
    print(f"Case #{tc}: {''.join(ans)}")