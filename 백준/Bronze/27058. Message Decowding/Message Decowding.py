key = input()
for c in input():
    if not c.isalpha():
        p = c
    elif c.isupper():
        p = key[ord(c) - 65].upper()
    else:
        p = key[ord(c) - 97]
    print(p, end='')