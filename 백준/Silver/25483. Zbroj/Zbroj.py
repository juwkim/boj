A, B, Z = map(int, open(0).read().split())
Min = (0, 10**(A - 1))[A > 1]
Min += max(0, Z - Min - 10**B + 1)
Max = 10**A - 1
Max -= max(0, (0, 10**(B - 1))[B > 1] - Z + Max)
cnt = Max - Min + 1
if A == B:
    if Z & 1:
        cnt >>= 1
    else:
        cnt = cnt + 1 >> 1
print(cnt)