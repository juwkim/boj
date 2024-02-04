def comp(a, b):
    return a[0].lower() == b[0].lower() and a[1:] == b[1:]

news = []
for _ in range(int(input())):
    name = input()
    words = [input() for _ in range(int(input()))]
    lines = []
    for _ in range(int(input())):
        tokens = []
        s = input()
        if not s:
            lines.append([])
            continue
        c, *line = s
        token, mode = [c], c.isalpha()
        for c in line:
            if mode == c.isalpha():
                token.append(c)
            else:
                tokens.append(''.join(token))
                token, mode = [c], not mode
        tokens.append(''.join(token))
        lines.append(tokens)
    news.append((name, words, lines))
for i, (name, _, lines) in enumerate(news):
    print(name)
    for tokens in lines:
        buf = []
        for token in tokens:
            if not token.isalpha():
                buf.append(token)
                continue
            for pi, (pname, _, _) in enumerate(news):
                if i == pi:
                    continue
                if comp(token, pname):
                    buf.append(f"[[{token}]]")
                    break
            else:
                for pi, (pname, words, _) in enumerate(news):
                    if i == pi:
                        continue
                    if any(comp(token, word) for word in words):
                        buf.append(f"[[{pname}|{token}]]")
                        break
                else:
                    buf.append(token)
        print(*buf, sep="")