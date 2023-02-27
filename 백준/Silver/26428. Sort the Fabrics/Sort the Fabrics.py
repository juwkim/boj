for case in range(1, int(input()) + 1):
    fabrics = [input().split() for _ in range(int(input()))]
    ada = sorted(fabrics, key=lambda f: (f[0], int(f[2])))
    charles = sorted(fabrics, key=lambda f: (int(f[1]), int(f[2])))
    same = sum(a[2] == c[2] for a, c in zip(ada, charles))
    print(f'Case #{case}:', same)