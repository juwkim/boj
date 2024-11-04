print("Case #1:")
s = open(0).read()
i, d = 0, 0
while i < len(s):
    if s[i:i+2] == "/*":
        d += 1
        i += 1
    elif d and s[i:i+2] == "*/":
        d -= 1
        i += 1
    elif d == 0:
        print(s[i], end='')
    i += 1