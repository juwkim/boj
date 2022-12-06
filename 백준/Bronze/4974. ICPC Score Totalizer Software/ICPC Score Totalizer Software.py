while n := int(input()):
    print(sum(sorted(int(input()) for _ in range(n))[1:-1]) // (n - 2))