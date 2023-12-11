import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while True:
    N, P = g()
    if N == 0:
        break
    stack = [[0], *[g() for _ in range(P)], [0]]
    
    x, y = -1, -1
    for i in range(1, P + 1):
        for j in range(1, stack[i][0] + 1):
            if stack[i][j] == 1:
                x, y = i, j
                break
        else:
            continue
        break
    assert x != -1 and y != -1
    
    ans = stack[x][0] - y
    t = x - 1
    cnt1 = 0
    while t >= 0 and stack[t][0] >= y:
        cnt1 += stack[t][0] - y + 1
        t -= 1
    
    t = x + 1
    cnt2 = 0
    while t <= P and stack[t][0] >= y:
        cnt2 += stack[t][0] - y + 1
        t += 1
    
    ans += min(cnt1, cnt2)
    print(ans)