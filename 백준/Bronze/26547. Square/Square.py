for _ in range(int(input())):
    s = input()
    print(s)
    i, j = 1, -2
    p = ' ' * (len(s) - 2)
    while i < len(s) - 1:
        print(s[i] + p + s[j])
        i += 1
        j -= 1
    if len(s) > 1:
        print(s[::-1])