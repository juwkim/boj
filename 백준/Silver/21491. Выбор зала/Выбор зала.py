A, B, C, D = map(int, input().split())
ans = 0
for i in range(1, int(B**.5) + 1):
    p = max((C + 1 >> 1) - i, (A + i - 1) // i, i)
    q = min(D // 2 - i, B // i)
    ans += max(0, q - p + 1)
print(ans)