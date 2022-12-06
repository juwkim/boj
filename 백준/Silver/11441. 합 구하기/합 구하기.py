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
N = int(input())
tree = [0] * (N + 1)

for idx, num in enumerate(g(), 1):
    update(idx, num)

for _ in range(int(input())):
    print(range_sum(*g()))