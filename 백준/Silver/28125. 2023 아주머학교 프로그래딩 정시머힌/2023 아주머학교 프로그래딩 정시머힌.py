table = {'@': 'a', '[': 'c', '!': 'i', ';': 'j', '^': 'n',
         '0': 'o', '7': 't'}
for _ in range(int(input())):
    s = input()
    ans = []
    i = 0
    a, b = 0, 0
    while i < len(s):
        if i < len(s) - 1 and s[i] == '\\' and s[i+1] == "'":
            ans.append('v')
            i += 2
            b += 1
        elif i < len(s) - 2 and s[i] == '\\' and s[i+1] == '\\' and s[i+2] == "'":
            ans.append('w')
            i += 3
            b += 1
        elif s[i] in table:
            ans.append(table.get(s[i]))
            i += 1
            b += 1
        else:
            ans.append(s[i])
            i += 1
            a += 1
    if b >= a:
        print("I don't understand")
    else:
        print(*ans, sep='')