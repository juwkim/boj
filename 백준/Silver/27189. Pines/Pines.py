l, r, f = 2, int(input()) + 1, True
print(1, end=' ')
for c in input():
    f ^= c == 'A'
    if f:
        print(l, end=' ')
        l += 1
    else:
        print(r, end=' ')
        r -= 1