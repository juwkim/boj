for _ in range(int(input())):
    s = input()
    t = len(s)
    l = int(t**.5)
    for i in range(l-1, -1, -1):
        for j in range(0, t, l):
            print(s[i+j], end='')
    print()