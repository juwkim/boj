while (s:= input()) != '#':
    ans = set()
    for word in s.split():
        if not any(c.isalpha() for c in word):
            continue
        tmp = []
        for c in word:
            if c.isalnum():
                tmp.append(c.lower())
        if tmp:
            ans.add(''.join(tmp))
    for word in sorted(ans):
        print(word)
    print()