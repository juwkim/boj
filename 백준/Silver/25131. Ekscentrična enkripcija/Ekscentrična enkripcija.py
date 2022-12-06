p = lambda a, b: (ord(b) - ord(a)) % 26
s, t = input(), input()
if len(s) != len(t):
    print(-1)
else:
    l = [p(s[i], t[i]) for i in range(3)]
    if all(l[i%3] == p(s[i], t[i]) for i in range(3, len(s))):
        print(*l)
    else:
        print(-1)