import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    F, R, N = g()
    building = [[0] * (R + 1) for _ in range(F + 1)]
    for _ in range(N):
        a, b = g()
        building[a][b] = 1
    ans = F * 2 + R + 1
    for i in range(1, F + 1):
        s, e = 1, 0
        l, r = None, None
        for j in range(1, R + 1): 
            if building[i][j]:
                if l:
                    r = j - 1
                    if r - l > e - s:
                        s, e = l, r
                    l = None
            else:
                if not l:
                    l = j
        if l:
            r = R
            if r - l > e - s:
                s, e = l, r
        ans += 2 * (s - 1 + R - e)
    print(ans)