import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
from collections import Counter

N = int(input())
parent = [*range(N)]
rank = [0] * N

def find(x):
    p = x
    while p != parent[p]:
        p = parent[p]
    parent[x] = p
    return p

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

def val(x1, y1, x2, y2, x):
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

nums = []
for i in range(N):
    x1, y1, x2, y2 = g()
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    for j in range(i):
        x3, y3, x4, y4 = nums[j]
        sx, ex = max(x1, x3), min(x2, x4)
        if sx > ex:
            continue
        if x1 == x2:
            a1, a2 = y1, y2
        else:
            a1, a2 = val(x1, y1, x2, y2, sx), val(x1, y1, x2, y2, ex)
        if x3 == x4:
            b1, b2 = y3, y4
        else:
            b1, b2 = val(x3, y3, x4, y4, sx), val(x3, y3, x4, y4, ex)
        # print((i, j), a1, a2, b1, b2)
        if (a1 - b1) * (a2 - b2) <= 0:
            union(i, j)
    nums.append((x1, y1, x2, y2))
for i in range(N):
    find(i)
group = sum(i == parent[i] for i in range(N))
print(group)
print(Counter(parent).most_common(1)[0][1])
# print(parent)