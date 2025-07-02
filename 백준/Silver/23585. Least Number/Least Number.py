N, d = map(int, input().split())
if d == 9:
    q, r = divmod(N, 8)
    digits = [8] * q
    if r: digits.append(r)
elif d == 0:
    q, r = divmod(N, 9)
    digits = [9] * q
    if r: digits.append(r)
else:
    digits = []
    while N > 9:
        digits.append(9)
        N -= 9
    if N == d:
        if digits and d != 8:
            digits[-1] -= 1
            digits.append(N + 1)
        else:
            digits.append(N - 1)
            digits.append(1)
    else:
        digits.append(N)
print(*digits[::-1], sep="")