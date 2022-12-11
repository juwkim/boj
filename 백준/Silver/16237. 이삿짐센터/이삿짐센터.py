A, B, C, D, E = map(int, input().split())
ans = C + D + E
if C > B:
    A -= 2 * (C - B) + D
    B = 0
else:
    A -= D
    B -= C
if B > 0:
    q, r = divmod(B, 2)
    ans += q
    A -= q
    if r == 1:
        ans += 1
        A -= 3
if A > 0:
    ans += (A + 4) // 5
print(ans)