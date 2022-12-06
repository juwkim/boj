X, Y = map(int, input().split())
Z = Y * 100 // X + 1
if Z >= 100:
    print(-1)
else:
    print((X * Z - 100 * Y + 99 - Z) // (100 - Z))