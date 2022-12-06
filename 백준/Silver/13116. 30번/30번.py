for _ in range(int(input())):
    A, B = sorted(map(int, input().split()))
    while A != B:
        A, B = sorted([A, B >> 1])
    print(10 * A)