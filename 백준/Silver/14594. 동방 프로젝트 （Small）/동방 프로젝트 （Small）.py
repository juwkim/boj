N = int(input())
buf = set()
for _ in range(int(input())):
    a, b = map(int, input().split())
    flag = True
    removed = set()
    for x, y in buf:
        if b < x or a > y:
            continue
        if x <= a and b <= y:
            flag = False
            break
        a, b = min(a, x), max(b, y)
        removed.add((x, y))
    buf -= removed
    if flag:
        buf.add((a, b))
ans = len(buf)
buf = [[0, 0]] + sorted(buf) + [[N + 1, N + 1]]
for i in range(len(buf) - 1):
    ans += buf[i+1][0] - buf[i][1] - 1
print(ans)
            