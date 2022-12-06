vowel = set('aeiou')
while (s:= input()) != 'end':
    if len(s) == 1:
        if s in vowel:
            ans = 'acceptable.'
        else:
            ans = 'not acceptable.'
    elif len(s) == 2:
        if s == 'ee' or s == 'oo':
            ans = 'acceptable.'
        elif s[0] == s[1]:
            ans = 'not acceptable.'
        elif s[0] in vowel or s[1] in vowel:
            ans = 'acceptable.'
        else:
            ans = 'not acceptable.'
    else:
        res = [i in vowel for i in s]
        if sum(res) == 0:
            ans = 'not acceptable.'
        elif any(i + j + k in [0, 3] for i, j, k in zip(res, res[1:], res[2:])):
            ans = 'not acceptable.'
        elif any(i == j and i not in 'eo' for i, j in zip(s, s[1:])):
            ans = 'not acceptable.'
        else:
            ans = 'acceptable.'
    print(f'<{s}> is', ans)