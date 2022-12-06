while (n := int(input())) + 1:
    temp = []
    for _ in range(n):
        a, b, c, name = input().split()
        area = int(a) * int(b) * int(c)
        temp.append((area, name))
    p, q = min(temp)[1], max(temp)[1]
    print(f'{q} took clay from {p}.')