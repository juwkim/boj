for _ in range(int(input())):
    l = [*map(int, input().split())]
    print(*l)
    print(("zilch", "double", "double-double", "triple-double")[sum(num >= 10 for num in l)])
    print()