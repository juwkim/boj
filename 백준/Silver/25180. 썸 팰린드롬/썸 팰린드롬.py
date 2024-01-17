q, r = divmod(int(input()), 18)
ans = 2 * q
if r == 0:
    pass
elif r <= 9:
    ans += 1
else:
    ans += 2 + (r&1)
print(ans)