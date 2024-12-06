ans, d, prv = 0, -1, None
for c in input():
    if c == '(':
        d += 1
    else:
        if prv == '(':
            ans += d
        d -= 1
    prv = c
print(ans)