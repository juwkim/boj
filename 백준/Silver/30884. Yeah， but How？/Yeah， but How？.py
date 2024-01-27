ans = []
s = input()
for a, b in zip(s, s[1:]):
    match a + b:
        case "((": ans.append('(')
        case "()": ans.append('(1')
        case ")(": ans.append(')+')
        case "))": ans.append(')')
ans.append(s[-1])
print(*ans, sep='')