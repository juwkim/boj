incord = {' ': '#'}
for _ in range(26):
    s = input()
    incord[s[0]] = s[1:]

decord = {value: key for key, value in incord.items()}
for _ in range(int(input())):
    s = input()
    i = 0
    ans = []
    while i < len(s):
        if s[i] == '#':
            ans.append(' ')
            i += 1
        elif s[i:i+2] in decord:
            ans.append(decord[s[i:i+2]])
            i += 2
        else:
            ans.append(decord[s[i:i+3]])
            i += 3
    print(*ans, sep='')

for _ in range(int(input())):
    ans = []
    for c in input():
        ans.append(incord[c])
    print(*ans, sep='')