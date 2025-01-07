N = int(input())
s = input()
l = [s[0]]
for i in range(1, N):
    p = s[i - 1] + s[i]
    match p:
        case ")(":
            l.append("*")
        case "()":
            l.append("1")
        case "))":
            l.append("+1")
    l.append(s[i])
print(eval("".join(l)))