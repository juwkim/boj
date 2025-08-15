s, t = input(), input()
i, j = len(s) - 1, len(t) - 1
ans = "YES"
while j >= 0:
    if i < 0:
        ans = "NO"
        break
    if s[i] == t[j]:
        i -= 1
        j -= 1
    else:
        i -= 2
if i % 2 == 0:
    ans = "NO"
print(ans)