g = lambda: [*map(int, input().split())]

tc = 1
while (arr:=g())[0]:
    h, w = arr
    a = [bytearray(w) for _ in range(h)]
    n, *nums = g()
    for i in range(0, 2 * n, 2):
        x, y = nums[i], nums[i + 1]
        a[x][y] = 1
    while (s:=input()) != "done":
        direction, m = s.split()
        m = int(m)
        match direction:
            case "left":
                for r in range(w - 1, w - 1 - m, -1):
                    if any(all(a[i][j] for j in range(r + 1)) for i in range(h)):
                        break
                    for i in range(h):
                        k = r
                        while k and a[i][k]:
                            k -= 1
                        a[i][k] = 1
                        a[i][r] = 0
            case "right":
                for l in range(m):
                    if any(all(a[i][j] for j in range(l, w)) for i in range(h)):
                        break
                    for i in range(h):
                        k = l
                        while k < w - 1 and a[i][k]:
                            k += 1
                        a[i][k] = 1
                        a[i][l] = 0
            case "up":
                for d in range(h - 1, h - 1 - m, -1):
                    if any(all(a[i][j] for i in range(d + 1)) for j in range(w)):
                        break
                    for j in range(w):
                        k = d
                        while k and a[k][j]:
                            k -= 1
                        a[k][j] = 1
                        a[d][j] = 0
            case "down":
                for u in range(m):
                    if any(all(a[i][j] for i in range(u, h)) for j in range(w)):
                        break
                    for j in range(w):
                        k = u
                        while k < h - 1 and a[k][j]:
                            k += 1
                        a[k][j] = 1
                        a[u][j] = 0
    print(f"Data set {tc} ends with boxes at locations", end='')
    for i in range(h):
        for j in range(w):
            if a[i][j]:
                print(f" ({i},{j})", end='')
    print('.')
    tc += 1