s, t = open(0)
ans, i, f = "YES", 0, False
while i < len(s) - 1:
    if s[i] == t[i]:
        i += 1
    elif s[i] == t[i + 1] and s[i + 1] == t[i]:
        if f:
            ans = "NO"
            break
        f = True
        i += 2
    else:
        ans = "NO"
        break
print(ans)