for _ in range(int(input())):
    a, b = sorted(map(int, input().split()))
    print(['No', 'Yes'][a + b <= 3 and b != 3])