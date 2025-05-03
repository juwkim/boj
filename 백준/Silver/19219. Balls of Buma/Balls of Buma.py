s = input()
l, r = 0, len(s) - 1
ans = 0
while l < r and s[l] == s[r]:
    p = l + 1
    while p < r and s[p] == s[l]: p += 1
    if p == r:
        ans = r - l + 2
        break
    q = r - 1
    while s[q] == s[l]: q -= 1
    if (r - l) - (q - p) < 3:
        break
    l, r = p, q
print(ans)