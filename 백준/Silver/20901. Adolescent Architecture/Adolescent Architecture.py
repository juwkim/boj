import sys
from functools import cmp_to_key
input = sys.stdin.readline

def can_contain(A, B):
    t1, x1 = A
    t2, x2 = B
    if t1[1] == t2[1]: return x1 <= x2
    if t1[1] == 'u': return x1 * x1 <= 2 * x2 * x2
    return 2 * x1 <= x2

def solve():
    n = int(input())
    blocks = []
    for _ in range(n):
        typ, a = input().split()
        blocks.append((typ, int(a)))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if not can_contain(blocks[i], blocks[j]) and not can_contain(blocks[j], blocks[i]):
                print("impossible")
                return
    def cmp(A, B):
        if can_contain(A, B):
            return -1
        return 1
    for typ, a in sorted(blocks, key=cmp_to_key(cmp)):
        print(typ, a)
solve()