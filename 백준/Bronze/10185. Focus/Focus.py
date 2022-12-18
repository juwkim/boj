for _ in range(int(input())):
    p, q = map(int, input().split())
    f = p * q / (p + q)
    print(f'f = {f:#.1f}')