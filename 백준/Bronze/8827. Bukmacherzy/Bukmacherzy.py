for _ in range(int(input())):
    A, B = map(float, input().split())
    print('TAK' if (A - 1) * (B - 1) > 1 else 'NIE')