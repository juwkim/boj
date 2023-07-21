s = input().lower()
idx = s.find("ss")
if idx == -1:
    print(s)
elif idx + 2 < len(s) and s[idx + 2] == 's':
    print(s)
    print(s[:idx] + 'B' + s[idx + 2:])
    print(s[:idx + 1] + 'B' + s[idx + 3:])
else:
    print(s)
    print(s.replace("ss", 'B'))