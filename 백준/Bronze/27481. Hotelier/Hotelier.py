ans = bytearray(10)
input()
for c in input():
    if c == 'L':
        for i in range(10):
            if ans[i] == 1:
                continue
            ans[i] = 1
            break
    elif c == 'R':
        for i in range(9, -1, -1):
            if ans[i] == 1:
                continue
            ans[i] = 1
            break
    else:
        ans[int(c)] = 0
print(*ans, sep='')