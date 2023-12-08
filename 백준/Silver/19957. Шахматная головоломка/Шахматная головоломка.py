r, c = input()
r = ord(r) - ord('a')
c = ord(c) - ord('1')
if r == 0:
    if c <= 3:
        a1, b1 = r, c + 3
        a2, b2 = r + 1, c + 1
    else:
        a1, b1 = r, c - 3
        a2, b2 = r + 1, c - 1
else:
    if c <= 3:
        a1, b1 = r, c + 3
        a2, b2 = r - 1, c + 1
    else:
        a1, b1 = r, c - 3
        a2, b2 = r - 1, c - 1

print(chr(a1 + ord('a')), b1 + 1, sep='')
print(chr(a2 + ord('a')), b2 + 1, sep='')