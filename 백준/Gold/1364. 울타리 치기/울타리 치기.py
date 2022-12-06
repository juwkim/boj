r, q = divmod(int(input()), 6)
ans = 0
if r:
    ans += 3 * r * (r + 1) + 1
    if q:
        ans += (r + 1) * q - 1
else:
    ans = q
print(ans)