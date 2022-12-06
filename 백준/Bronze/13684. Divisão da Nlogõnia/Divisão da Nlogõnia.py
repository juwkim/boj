while (K := int(input())):
    N, M = map(int, input().split())
    for _ in range(K):
        X, Y = map(int, input().split())
        if X > N:
            print(['divisa', 'NE', 'SE'][(Y > M) - (Y < M)])
        elif X < N:
            print(['divisa', 'NO', 'SO'][(Y > M) - (Y < M)])
        else:
            print('divisa')