c, *s = input()
l = [c]
for c in s:
    if c != l[-1]:
        l.append(c)
print("".join(l[:2 + (len(l) & 1)]))