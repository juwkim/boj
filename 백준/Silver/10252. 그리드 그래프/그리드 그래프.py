for _ in range(int(input())):
    m, n = map(int, input().split())
    print(1)
    if m % 2 == 0:
        for i in range(0, m - 1, 2):
            for j in range(n):
                print(f"({i},{j})")
            for j in range(n - 1, -1, -1):
                print(f"({i + 1},{j})")
    elif n % 2 == 0:
        for j in range(0, n - 1, 2):
            for i in range(m):
                print(f"({i},{j})")
            for i in range(m - 1, -1, -1):
                print(f"({i},{j + 1})")
    else:
        for i in range(0, m - 2, 2):
            for j in range(n - 1):
                print(f"({i},{j})")
            for j in range(n - 2, -1, -1):
                print(f"({i + 1},{j})")
        for j in range(n):
            print(f"({m - 1},{j})")
        for i in range(m - 2, -1, -1):
            print(f"({i},{n - 1})")