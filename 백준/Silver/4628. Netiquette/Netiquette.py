while (s:=input()) != '#':
    s = ' ' + s + ' '
    ans = "OK"
    for i in range(1, len(s) - 1):
        if s[i].isupper() and s[i + 1].isupper():
            ans = "suspicious"
            break
        if s[i].isdigit() and (s[i - 1].isalpha() or s[i + 1].isalpha()):
            ans = "suspicious"
            break
        if (s[i] not in " aAI") and (s[i - 1] == ' ' and s[i + 1] == ' '):
            ans = "suspicious"
            break
        if (s[i] not in ' "' and not s[i].isalnum()) and (s[i + 1] not in ' "' and not s[i + 1].isalnum()):
            ans = "suspicious"
            break
    print(ans)