while (s := input()) != '#':
    if all((ord(b) - ord(a)) % 7 in range(2, 7, 2) for a, b in zip(s, s[1:])):
        print('That music is beautiful.')
    else:
        print('Ouch! That hurts my ears.')