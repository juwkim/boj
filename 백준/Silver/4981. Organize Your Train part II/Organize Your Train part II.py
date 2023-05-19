for _ in range(int(input())):
    check = set()
    s = input()
    for i in range(1, len(s)):
        a, b = s[:i], s[i:]
        for p, q in ((a, b), (a, b[::-1]), (a[::-1], b), (a[::-1], b[::-1])):
            check.add(p + q)
        b, a = s[:i], s[i:]
        for p, q in ((a, b), (a, b[::-1]), (a[::-1], b), (a[::-1], b[::-1])):
            check.add(p + q)
    print(len(check))