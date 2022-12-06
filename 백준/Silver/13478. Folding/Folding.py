g = lambda: [*map(int, input().split())]

W, H = sorted(g())
w, h = sorted(g())

def check(a, b, c, d):
    ans = 0
    while a < b:
        ans += 1
        a *= 2
    while c < d:
        ans += 1
        c *= 2
    return ans

if W >= w and H >= h:
    ans = min(check(w, W, h, H), check(w, H, h, W))
else:
    ans = -1
print(ans)