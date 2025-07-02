N, d = map(int, input().split())
if d == 9:
    q, r = divmod(N, 8)
    digits = [8] * q
    if r: digits.append(r)
else:
    q, r = divmod(N, 9)
    digits = [9] * q
    if r:
        if r == d:
            if digits and d != 8:
                digits[-1] -= 1
                digits.append(r + 1)
            else:
                digits.append(r - 1)
                digits.append(1)
        else:
            digits.append(r)
print(*digits[::-1], sep="")