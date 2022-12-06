for i in range(1, 1+int(input())):
    print(f'Case {i}:')
    n = int(input())
    j = 1
    while j <= n - j:
        if n - j <= 6:
            print(f'({j},{n-j})')
        j += 1