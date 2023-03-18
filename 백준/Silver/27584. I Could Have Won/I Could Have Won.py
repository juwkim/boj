s = input()
ans = []
for k in range(1, len(s) + 1):
    
    alice, bob = 0, 0
    A, B = 0, 0
    for c in s:
        if c == 'A':
            A += 1
            if A == k:
                alice += 1
                A, B = 0, 0
        else:
            B += 1
            if B == k:
                bob += 1
                A, B = 0, 0
    if alice > bob:
        ans.append(k)
print(len(ans))
print(*ans)