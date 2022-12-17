for _ in range(int(input())):
    a, b = map(int, input().split())
    for _ in range(b):
        print('X' * a)
    print()