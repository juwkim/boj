s=input()
print(s[0], end='')
for a,b in zip(s,s[1:]):
    if a != b:
        print(b, end='')