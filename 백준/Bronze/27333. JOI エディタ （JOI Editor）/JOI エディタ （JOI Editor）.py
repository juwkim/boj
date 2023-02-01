input()
ans = []
for c in input():
    if ans and ans[-1] == c:
        ans[-1] = ans[-1].upper()
        ans.append(c.upper())
    else:
        ans.append(c)
print(*ans, sep='')