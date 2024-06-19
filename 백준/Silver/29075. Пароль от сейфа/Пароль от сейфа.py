l = len(s:=input())
a = [sorted((s[i], s[l - 1 - i])) for i in range(l // 2) if s[i] != s[l - 1 - i]]
ans = "NO"
match len(a):
    case 0:
        ans = "YES"
    case 1:
        if l & 1 and s[l // 2] in a[0]:
            ans = "YES"
    case 2:
        if a[0] == a[1]:
            ans = "YES"
print(ans)