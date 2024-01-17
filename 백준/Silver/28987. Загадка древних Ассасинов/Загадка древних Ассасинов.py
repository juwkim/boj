s = sorted([int(i) for i in input()], reverse=True)
Sum = sum(s)
r = Sum % 3
if r:
    div = [[], [], []]
    for i in range(len(s)):
        div[s[i] % 3].append(i)
    if r == 1:
        if div[1]:
            s.pop(div[1][-1])
        else:
            s.pop(div[2][-1])
            s.pop(div[2][-2])
    else: # r == 2
        if div[2]:
            s.pop(div[2][-1])
        else:
            s.pop(div[1][-1])
            s.pop(div[1][-2])
print(*s, sep='')