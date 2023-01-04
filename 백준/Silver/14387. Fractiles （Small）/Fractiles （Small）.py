for t in range(1, 1 + int(input())):
    k, c, s = map(int, input().split())
    ans = [*range(1, 1 + s * k ** (c - 1), k ** (c - 1))]
    print(f'Case #{t}:', *ans)