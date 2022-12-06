for _ in range(int(input())):
    n, s, *p = input().split()
    for password in p:
        i, k = 0, 0
        decoded = ''
        while i < len(password):
            if password[i] == '1':
                k = 2*k + 2
            else:
                k = 2*k + 1
            if s[k] != '*':
                decoded += s[k]
                k = 0
            i += 1
        print(decoded, end=' ')
    print()