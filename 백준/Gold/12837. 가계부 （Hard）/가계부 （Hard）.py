import sys
input = sys.stdin.readline
def point_sum(idx):
    res = 0
    while idx:
        res += tree[idx]
        idx -= idx & -idx
    return res

def range_sum(s, e):
    return point_sum(e) - point_sum(s-1)


def update(idx, num):
    while idx <= N:
        tree[idx] += num
        idx += idx & -idx
        

g = lambda: [*map(int, input().split())]
N, Q = g()
tree = [0] * (N + 1)

for _ in range(Q):
    cmd, a, b = g()
    if cmd == 1:
        update(a, b)
    else:
        print(range_sum(a, b))