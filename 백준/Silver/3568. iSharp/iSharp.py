base, *s = input().split()
for val in s:
    ans = []
    idx = -2
    while True:
        if val[idx] in '*&':
            ans.append(val[idx])
            idx -= 1
        elif val[idx] == ']':
            ans.append('[]')
            idx -= 2
        else:
            break
    print(base + ''.join(ans), val[:idx+1] + ';')