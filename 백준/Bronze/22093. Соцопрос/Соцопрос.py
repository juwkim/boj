for _ in range(int(input())):
    n, a, b = map(int, input().split())
    print(min(max(0, a - b), n - b), min(a, n - b))