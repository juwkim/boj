buf = []
for i in range(1, 1 + int(input())):
    num = 0
    A = 0
    for c in input():
        if c.isnumeric():
            num += int(c)
        elif c == 'A':
            A += 1
            num += 1
        else:
            num += 10
    if A >= 2 and num <= 1:
        num += 20
    elif A >= 1 and num <= 11:
        num += 10
    if num <= 21:
        buf.append((i, num))
if not buf:
    print(0)
else:
    Max = max([line[1] for line in buf])
    ans = []
    for line in buf:
        if line[1] == Max:
            ans.append(line[0])
    print(len(ans))
    print(*ans)