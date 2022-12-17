for _ in range(int(input())):
    ans = 0
    for _ in range(int(input())):
        _, a, b = input().split()
        ans += int(a) * float(b)
    print(f'${ans:#.2f}')