for _ in range(int(input())):
    s, k, i = input(), -1, -1
    LDS = ''
    while i + len(s) >= 0 and ord(s[i]) > k:
        LDS = s[i] + LDS
        k, i = ord(s[i]), i - 1

    print(f'The longest decreasing suffix of {s} is {LDS}')