input()
ans, cur, prv = 0, 0, None
for c in input():
    if prv:
        if prv + c in ("ah", "ha"):
            cur += 1
            prv = c
        else:
            ans = max(ans, cur)
            if c in "ah":
                cur, prv = 1, c
            else:
                cur, prv = 0, None
    elif c in "ah":
        cur, prv = 1, c
print(max(ans, cur))