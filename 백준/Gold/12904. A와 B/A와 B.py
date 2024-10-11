S, T = input(), input()
l, r = 0, len(T) - 1
isfront = True
for _ in range(len(T) - len(S)):
    if isfront:
        if T[r] == 'B':
            isfront = False
        r -= 1
    else:
        if T[l] == 'B':
            isfront = True
        l += 1
if isfront:
    print(+(S == T[l:r + 1]))
else:
    print(+(S == T[r:l - 1:-1]) if l else +(S == T[r::-1]))