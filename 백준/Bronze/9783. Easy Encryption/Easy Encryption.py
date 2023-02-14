ans = []
for c in input():
    if c.isnumeric():
        ans.append(f'#{c}')
    elif c.islower():
        ans.append(f'{ord(c) - 96:#02d}')
    elif c.isupper():
        ans.append(f'{ord(c) - 38:#02d}')
    else:
        ans.append(c)
print(*ans, sep="")