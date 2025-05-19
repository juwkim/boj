import sys
input = sys.stdin.readline

n, m, s, p, q = map(int, input().split())
pre_selected = set(int(input()) for _ in range(p))
desired = set(int(input()) for _ in range(q))
min_page, max_page = 1e9, -1e9
ans = 0
for page in range((n + m - 1) // m):
    start, end = page * m + 1, min(n, (page + 1) * m)
    items = set(range(start, end + 1))
    pre = pre_selected & items
    want = desired & items
    if pre != want:
        min_page = min(min_page, page)
        max_page = max(max_page, page)
    ans += min(len(pre ^ want), 1 + len(want), end + 2 - start - len(want))
a, b = max(0, s - min_page - 1), max(0, max_page - s + 1)
ans += a + b + min(a, b)
print(ans)