from collections import Counter
from itertools import pairwise

def solve():
    N = int(input())
    A, B, C, D = map(int, input().split())
    cnt = Counter(S:=input())
    if S[0] != 'a' or S[-1] != 'a':
        return "No"
    if cnt['a'] > A or cnt['b'] > B or cnt['c'] > C or cnt['d'] > D:
        return "No"
    if any(a == b for a, b in pairwise(S)):
        return "No"
    return "Yes"

print(solve())