import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = [*map(int, input().split())]
group, id = [-1] * n, 0
for i in range(n):
    if group[i] != -1: continue
    group[i], cur = id, p[i] - 1
    while cur != i:
        group[cur] = id
        cur = p[cur] - 1
    id += 1
if group[1] == 1:
    for i in range(1, n):
        if group[i] == 1: group[i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    print(("No", "Yes")[group[a-1] == group[b-1]])