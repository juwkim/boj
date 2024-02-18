if input() == '1':
    num = sum(map(int, input().split()))
    buf = []
    num, c = divmod(num, 25)
    buf.append(chr(c + 97))
    while num:
        num, c = divmod(num, 26)
        buf.append(chr(c + 97))
    ans = "".join(reversed(buf))
    if len(ans) < 13:
        ans += "z" * (13 - len(ans))
    print(ans)
else:
    ans = 0
    *s, e = input().rstrip('z')
    for c in s:
        ans = ans * 26 + ord(c) - 97
    ans = ans * 25 + ord(e) - 97
    print(ans)