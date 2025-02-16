import sys
input = sys.stdin.readline

n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
P = [None] * n
for i in range(n):
    x, y, s = nums[i]
    js, m = [], s
    for j in range(n):
        if i == j:
            continue
        p = nums[j][2] / ((x - nums[j][0]) ** 2 + (y - nums[j][1]) ** 2)
        if p > m:
            js, m = [j], p
        elif js and p == m:
            js.append(j)
    if len(js) == 0:
        P[i] = 'K'
    elif len(js) == 1:
        P[i] = js[0]
    else:
        P[i] = 'D'

for l in P:
    if l == 'D' or l == 'K':
        print(l)
    else:
        while type(P[l]) == int:
            l = P[l]
        print(l + 1)