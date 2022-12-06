K, P = 0, 0
for c in input():
    if c == 'K':
        K += 1
        if P:
            P -= 1
    else:
        P += 1
        if K:
            K -= 1
print(K + P)