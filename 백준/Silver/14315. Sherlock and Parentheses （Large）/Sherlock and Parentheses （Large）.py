for _ in range(1, 1 + int(input())):
    num = min(map(int, input().split()))
    print(f'Case #{_}:', num * (num + 1) // 2)