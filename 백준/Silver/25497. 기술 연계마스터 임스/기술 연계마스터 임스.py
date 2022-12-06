input()

ans = 0
L, S = 0, 0
for c in input():
    if c == 'L':
        L += 1
    elif c == 'S':
        S += 1
    elif c == 'R':
        if L:
            ans += 1
            L -= 1
        else:
            break
    elif c == 'K':
        if S:
            ans += 1
            S -= 1
        else:
            break
    else:
        ans += 1
print(ans)