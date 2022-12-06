for _ in range(int(input())):
    a, b = [0, 0, 0, 0], [0, 0, 0, 0]
    for _ in range(int(input())):
        u, v = map(int, input().split())
        a[u] += 1
        a[v] += 1
    for _ in range(int(input())):
        u, v = map(int, input().split())
        b[u] += 1
        b[v] += 1
    print('yes' if sorted(a) == sorted(b) else 'no')