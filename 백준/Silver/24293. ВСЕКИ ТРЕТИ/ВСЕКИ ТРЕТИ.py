s = input()
while len(s) >= 3:
    buf = []
    for i in range(len(s)):
        if i % 3 == 2:
            continue
        buf.append(s[i])
    s = ''.join(reversed(buf))
print(*sorted(s), sep='')