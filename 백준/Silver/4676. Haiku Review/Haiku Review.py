def count(line):
    num = 0
    flag = True
    for c in line:
        if c in 'aeiouy':
            num += flag
            flag = False
        else:
            flag = True
    return num

while (s:= input()) != 'e/o/i':
    l = (5, 7, 5)
    ans = 'Y'
    for i, line in enumerate(s.split('/')):
        if count(line) != l[i]:
            ans = i + 1
            break
    print(ans)