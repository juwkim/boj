input()
s = input()
p = []
for c in s:
    if c.isalpha():
        p.append(c)
    elif c == '0':
        continue
    else:
        p[-1] += c
i, ans = 0, []
for i in range(len(p)):
    match p[i]:
        case 'A+':
            ans.append('E')
        case 'A':
            if i and p[i - 1] in ('A+', 'A'):
                ans.append('P')
            else:
                ans.append('E')
        case 'A-' | 'B+':
            if i and p[i - 1] in ('A+', 'A', 'A-', 'B+'):
                ans.append('D')
            else:
                ans.append('P')
        case 'B' | 'B-':
            if i and p[i - 1] in ('A+', 'A', 'A-', 'B+', 'B', 'B-'):
                ans.append('B')
            else:
                ans.append('D')
        case _:
            ans.append('B')
print(*ans, sep='')