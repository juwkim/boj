A, B = map(int, input().split())
ans = 0
if A % 2 == 0:
    ans += 1
    A += 1
if B & 1:
    ans += 1
    B -= 1
if B > A:
    ans += (B - A + 1) // 2
print(ans)