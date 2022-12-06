for _ in range(int(input())):
    a, b = input().split()
    b = int(b)
    print(f'Shifting {a} by {b} positions gives us: {a[-b:]+a[:-b]}')