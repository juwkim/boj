mod = 10 ** 9 + 7
for _ in range(int(input())):
    ans, s = 1, None
    st = input()
    for idx, c in enumerate(st):
        if c == '?':
            if s == None:
                s = idx
        elif s != None:
            if s != 0 and st[s - 1] != st[idx]:
                ans = ans * (idx - s + 1) % mod
            s = None
    print(ans)