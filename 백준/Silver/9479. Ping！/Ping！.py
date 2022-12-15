while (s:= input()) != '0':
    ans = [int(i) for i in s]
    for i in range(1, len(ans)):
        if not ans[i]:
            continue
        print(i, end=' ')
        for j in range(2 * i, len(ans), i):
            ans[j] ^= 1
    print()