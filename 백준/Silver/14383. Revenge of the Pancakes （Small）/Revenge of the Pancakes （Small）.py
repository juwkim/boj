for step in range(1, 1 + int(input())):
    s = input()
    ans = - (s[0] == '-')
    t = s.split('+')
    ans += 2 * (len(t) - t.count(''))
    print(f'Case #{step}: {ans}')