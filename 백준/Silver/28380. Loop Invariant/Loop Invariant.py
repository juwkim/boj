s = input()
d, start = 0, 0
check = set()
ans = "no"
for i in range(len(s)):
    if s[i] == '(':
        d += 1
    else:
        d -= 1
        if d == 0:
            p = s[start:i + 1]
            if check and p not in check:
                ans = s[start:] + s[:start]
                break
            check.add(p)
            start = i + 1
print(ans)