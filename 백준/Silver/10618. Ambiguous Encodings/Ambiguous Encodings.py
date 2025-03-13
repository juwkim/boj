for tc in range(1, 1 + int(input())):
    s = input()
    dp = [0] * (len(s) + 1)
    a, b, c = 0, 0, 1
    for i in range(1, len(s) + 1):
        a, b, c = b, c, 0
        if s[i - 1] != '0':
            c = b
        if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
            c += a
        c &= 0xFFFFFFFFFFFFFFFF
    print(f"Case #{tc}: {c}")