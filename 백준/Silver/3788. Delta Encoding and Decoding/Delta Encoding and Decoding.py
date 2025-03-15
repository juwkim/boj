a = {}
for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    a[c] = i
b = {v: k for k, v in a.items()}
for l in open(0):
    idx = l.find(' ')
    if idx == -1:
        print("Command not understood.")
        continue
    cmd = l[:idx].upper()
    s = l[idx+1:].strip()
    match cmd:
        case "ENCRYPT":
            buf, prv = [], 'A'
            for c in s:
                if c.isalpha():
                    p = b[(a[c.upper()] - a[prv]) % 26]
                    if c.islower():
                        p = p.lower()
                    buf.append(p)
                    prv = c.upper()
                else:
                    buf.append(c)
                    prv = 'A'
            ans = f"RESULT:  {''.join(buf)}"
        case "DECRYPT":
            buf, prv = [], 'A'
            for c in s:
                if c.isalpha():
                    p = b[(a[c.upper()] + a[prv]) % 26]
                    if c.islower():
                        p = p.lower()
                    buf.append(p)
                    prv = p.upper()
                else:
                    buf.append(c)
                    prv = 'A'
            ans = f"RESULT:  {''.join(buf)}"
        case "CIPHER":
            alpha = [c.upper() for c in s if c.isalpha()]
            a = {}
            if len(alpha) == 26 and len({*alpha}) == 26:
                ans = f"Good cipher.  Using {''.join(alpha)}."
                for i, c in enumerate(alpha):
                    a[c] = i
            else:
                ans = "Bad cipher.  Using default."
                for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                    a[c] = i
            b = {v: k for k, v in a.items()}
        case _:
            ans = "Command not understood."
    print(ans)