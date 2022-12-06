A, B = map(int, input().split())
if (A+B) % 2 or (A - B) / 2 < 0:
    print(-1)
else:
    print((A + B) // 2, (A - B) // 2)