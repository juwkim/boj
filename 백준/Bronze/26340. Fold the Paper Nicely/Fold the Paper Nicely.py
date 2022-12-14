for _ in range(int(input())):
    *l, n = map(int, input().split())
    print('Data set:', *l, n)
    r, c = sorted(l, reverse=True)
    for _ in range(n):
        r, c = sorted([r // 2, c], reverse=True)
    print(r, c)
    print()