dic = {'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', 'b': 'd', 'd': 'b', 'i': 'i', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'q', 'q': 'p', 'r': '7', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', '0': '0', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '7': 'r', '8': '8'}

s = [*input()]
good = True
for i in range(len(s) >> 1):
    if dic.get(s[i].lower(), '') == s[-i - 1].lower():
        s[i] = s[i].lower()
        s[-i - 1] = s[-i - 1].lower()
    elif dic.get(s[i].upper(), '') == s[-i - 1].upper():
        s[i] = s[i].upper()
        s[-i - 1] = s[-i - 1].upper()
    else:
        good = False
        break
if len(s) & 1:
    c = s[len(s) >> 1]
    if dic.get(c.lower(), '') == c.lower():
        s[len(s) >> 1] = c.lower()
    elif dic.get(c.upper(), '') == c.upper():
        s[len(s) >> 1] = c.upper()
    else:
        good = False
if good:
    print(*s, sep='')
else:
    print(-1)