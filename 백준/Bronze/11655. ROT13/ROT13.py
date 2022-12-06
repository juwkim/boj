def ROT13(s):
    if s.isalpha():
        t = ord('A') + 32 * s.islower()
        return chr((ord(s) + 13 - t) % 26 + t)
    else:
        return s

print(*map(ROT13, input()), sep="")