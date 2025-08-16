for line in open(0):
    k, x, y = map(int, line.split())
    if k == 0:
        break
    sizes = [k]
    while k != 1:
        k >>= 1
        sizes.append(k)
    ans = 0
    rx, ry = abs(x - 1024), abs(y - 1024)
    for s in sizes:
        ans += rx <= s and ry <= s
        rx, ry = abs(rx - s), abs(ry - s)
    print(ans)