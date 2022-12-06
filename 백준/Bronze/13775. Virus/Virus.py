k, encrypted = int(input()), input()
decrypted, i = '', 0
for s in encrypted:
    if 96 < ord(s) < 123:
        decrypted += chr(97+(ord(s)-(k+i-1)%25-98)%26)
        i += 1
    else:
        decrypted += s
print(decrypted)