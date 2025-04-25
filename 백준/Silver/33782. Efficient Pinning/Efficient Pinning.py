import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

w, h = g()
a = [input() for _ in range(h)]
n, m = g()
b = [input() for _ in range(m)]
ans = 0
for i in range(h + 1 - m):
    for j in range(w + 1 - n):
        ok = True
        for k in range(m):
            if any(s != t and t != '*' for s, t in zip(a[i + k][j:j + n], b[k])):
                ok = False
                break
        if ok:
            ans += 1
print(ans)