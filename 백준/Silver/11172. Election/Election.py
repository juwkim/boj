for _ in range(int(input())):
    buf = []
    n = int(input())
    for _ in range(n):
        name, *l = input().split()
        x, y, r = map(int, l)
        buf.append((name, x, y, r))
    res = [0] * n
    for i in range(n-1):
        for j in range(i+1, n):
            name1, x1, y1, r1 = buf[i]
            name2, x2, y2, r2 = buf[j]
            flag = ((x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 + r2) ** 2)
            res[i] += flag
            res[j] += flag
    max_val = max(res)
    check = [i for i in range(n) if res[i] == max_val]
    print(buf[check[0]][0] if len(check) == 1 else 'TIE')