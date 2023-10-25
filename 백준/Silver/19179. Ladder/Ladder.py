import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n, k, x, y = g()
    if k:
        l = sorted([[x, 2], [y, k]])
    else:
        l = [[x, 2]]
    cur = 0
    ans = 'NO'
    for num in sorted(g()):
        if num < l[cur][0]:
            continue
        l[cur][1] -= 1
        if l[cur][1]:
            continue
        cur += 1
        if cur == len(l):
            ans = 'YES'
            break
    print(ans)