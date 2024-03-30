import sys
input = sys.stdin.readline

n = int(input())
buf = []
for _ in range(n):
    b, *l = input().split()
    r, s, u, d = map(int, l)
    buf.append((b, r, s, u, d))

ans = [['.' ] * 200 for _ in range(200)]
i, j = 0, 0
p, q = 0, 0
for num in map(int, input().split()):
    b, r, s, u, d = buf[num - 1]
    for x in range(i, i + r):
        for y in range(j, j + s):
            ans[x][y] = b
    p = max(p, i + r)
    q = max(q, j + s)
    if u:
        i, j = i + r - d, j + s
    else:
        i, j = i + r, j + d - 1
print(p, q)
for l in ans[:p][::-1]:
    print(*l[:q], sep='')