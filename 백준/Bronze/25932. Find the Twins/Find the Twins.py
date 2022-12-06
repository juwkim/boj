for _ in range(int(input())):
    s = input()
    idx = ('17' in s) + 2 * ('18' in s)
    print(s)
    print(['none', 'zack', 'mack', 'both'][idx])
    print()