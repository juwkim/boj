A, B, C, D, k = map(int, input().split())
if (A + C - 1) // k == (B + D) // k:
    print(-1)
else:
    num = (B + D) // k * k
    if num - B >= C:
        print(B, num - B)
    else:
        print(num - C, C)