for _ in range(int(input())):
    a, b = 0, 0
    for d in map(int, input().split()): a, b = max(a, b), a + d
    print(max(a, b))