import sys
input = sys.stdin.readline
mod = 1_000_000_007
mul = lambda a, b: a * b % mod


def point_sum(tree, idx):
    res = 0
    while idx:
        res += tree[idx]
        idx -= idx & -idx
    return res

def range_sum(tree, s, e):
    return point_sum(tree, e) - point_sum(tree, s-1)


def update_sum(tree, idx, num):
    while idx <= N:
        tree[idx] += num
        idx += idx & -idx
        
        
def point_mul(tree, idx):
    res = 1
    while idx:
        res = mul(res, tree[idx])
        idx -= idx & -idx
    return res


def range_mul(tree, s, e):
    return mul(point_mul(tree, e), pow(point_mul(tree, s-1), -1, mod))


def update_mul(tree, idx, num):
    while idx <= N:
        tree[idx] = mul(tree[idx], num)
        idx += idx & -idx

g = lambda: [*map(int, input().split())]
N, *l = g()
tree_sum = [0] * (N + 1)
tree_mul = [1] * (N + 1)

for i in range(1, N+1):
    val = int(input())
    if val == 0:
        update_sum(tree_sum, i, 1)
    else:
        update_mul(tree_mul, i, val)

for _ in range(sum(l)):
    a, b, c = g()
    if a == 1:
        temp = range_sum(tree_sum, b, b)
        if temp == 0:
            if c == 0:
                update_sum(tree_sum, b, 1)
            else:
                update_mul(tree_mul, b, pow(range_mul(tree_mul, b, b), -1, mod))
                update_mul(tree_mul, b, c)
        else:
            if c == 0:
                pass
            else:
                update_sum(tree_sum, b, -1)
                update_mul(tree_mul, b, pow(range_mul(tree_mul, b, b), -1, mod))
                update_mul(tree_mul, b, c)
    else:
        print(0 if range_sum(tree_sum, b,c) else range_mul(tree_mul, b, c))