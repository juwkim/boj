r, c = input()
r = ord(r)
c = ord(c)
if r == ord('a'):
    if c <= ord('4'):
        a1, b1 = r, c + 3
        a2, b2 = r + 1, c + 1
    else:
        a1, b1 = r, c - 3
        a2, b2 = r + 1, c - 1
else:
    if c <= ord('4'):
        a1, b1 = r, c + 3
        a2, b2 = r - 1, c + 1
    else:
        a1, b1 = r, c - 3
        a2, b2 = r - 1, c - 1

print(chr(a1), chr(b1), sep='')
print(chr(a2), chr(b2), sep='')