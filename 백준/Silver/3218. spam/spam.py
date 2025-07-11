import re

s = input()
candidates = [s]
for m in re.finditer('nospam', s):
    pos = m.start()
    candidates.append(s[:pos] + s[pos+6:])
ans = set()
for candidate in candidates:
    for m in re.finditer('at', candidate):
        pos = m.start()
        email = candidate[:pos] + '@' + candidate[pos+2:]
        if pos and pos != len(email) - 1 and email[pos - 1].isalpha() and email[pos + 1].isalpha() and email[0] != '.' and email[-1] != '.':
            ans.add(email)

for email in ans:
    print(email)