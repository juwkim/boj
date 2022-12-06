A, B, C = 0, 0, 0
for _ in range(int(input())):
    a, b, c = [*map(int, input().split())]
    A, B, C = A + a, B + b, C + c
    today = min([A, B, C])
    if today < 30:
        print('NO')
    else:
        print(today)
        A, B, C = map(lambda x: x - today, [A, B, C])