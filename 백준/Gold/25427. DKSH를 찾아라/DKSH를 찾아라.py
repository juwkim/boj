N = int(input())
D, K, S, H = 0, 0, 0, 0
for c in input():
    if c == 'D':
        D += 1
    elif c == 'K':
        K += D
    elif c == 'S':
        S += K
    elif c == 'H':
        H += S
print(H)