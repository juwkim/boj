P, S = input().split()
i = 0
for c in S:
    if c == P[i]:
        i += 1
    elif c in P[i+1:]:
        break
    if i == len(P):
        break
if i == len(P):
    print('PASS')
else:
    print('FAIL')