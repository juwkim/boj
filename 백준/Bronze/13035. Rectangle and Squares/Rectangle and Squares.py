for _ in range(int(input())):
    A, B, C = map(int, input().split())
    area1, area2 = A * B, C * C
    r, q = divmod(area1, area2)
    r += (2 * q > area2)
    print(r * area2 if r else area2)