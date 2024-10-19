import sys
input = lambda: sys.stdin.readline().rstrip()

h, w = map(int, input().split())
ans = 0
for _ in range(h):
    open, cnt = False, 0
    for c in input():
        if c == '.':
            if open:
                cnt += 1
        elif open:
            ans += cnt + 1
            cnt = 0
            open = False
        else:
            open = True
print(ans)