g = lambda: [*map(int, input().split())]

N = int(input())
ans = 0
cnt = 0
win = -1
for A, B in zip(g(), g()):
    res = (A - B) % 3
    if res == 0:
        win ^= 1
        ans = max(ans, cnt)
        cnt = 1
    elif res == 1:
        if win == 0:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
        win = 0
    else:
        if win == 1:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
        win = 1
print(max(ans, cnt))