ans = []
key = [ord(i) - 65 for i in input()]
idx = 0
for c in input():
    if not c.isalpha():
        continue
    s = chr(((ord(c) + key[idx]) - 65) % 26 + 65)
    ans.append(s)
    idx = (idx + 1) % len(key)
print(*ans, sep='')