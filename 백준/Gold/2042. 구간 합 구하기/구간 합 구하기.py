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

N, *l = g()
tree = [0] * (N + 1)

for i in range(1, N+1):
    update(i, int(input()))

for _ in range(sum(l)):
    a, b, c = g()
    if a == 1:
        update(b, c - range_sum(b, b))
    else:
        print(range_sum(b, c))