def point_sum(idx):
    res = 0
    while idx:
        res += tree[idx]
        idx -= idx & -idx
    return res

def range_sum(s, e):
    return point_sum(e) - point_sum(s-1)


def get_num(idx):
    return range_sum(idx, idx)


def update(idx, num):
    while idx <= N:
        tree[idx] += num
        idx += idx & -idx
        
import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
N, M = g()
tree = [0] * (N + 1)

for _ in range(M):
    a, b, c = g()
    if a == 1:
        update(b, c - get_num(b))
    else:
        print(range_sum(*sorted([b, c])))