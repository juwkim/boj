s = input()

if int(s[:2]) < 20:
    if s[6] == '-':
        prefix = '20'
    else:
        prefix = '19'
else:
    if s[6] == '-':
        prefix = '19'
    else:
        prefix = '18'

print(prefix + s[:6] + s[7:])