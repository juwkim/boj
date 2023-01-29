X = int(input())
man = 0
s = list(input())[::-1]
ans = len(s)
for i in range(len(s) - 1, -1, -1):
    if s[-1] == 'M':
        if man < X:
            man += 1
            s.pop()
        elif len(s) >= 2 and s[-2] == 'W':
            man -= 1
            tmp = s.pop()
            s.pop()
            s.append(tmp)
        else:
            break
    else:
        if man > -X:
            man -= 1
            s.pop()
        elif len(s) >= 2 and s[-2] == 'M':
            man += 1
            tmp = s.pop()
            s.pop()
            s.append(tmp)
        else:
            break

print(ans - len(s))