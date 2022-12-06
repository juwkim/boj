for i in range(1, 1 + int(input())):
    input()
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()), reverse=True)
    s = sum(x * y for x, y in zip(a, b))
    print(f'Case #{i}: {s}')