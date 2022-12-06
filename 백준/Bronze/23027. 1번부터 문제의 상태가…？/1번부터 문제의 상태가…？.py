S = input()
if 'A' in S:
    for i in 'BCDF':
        S = S.replace(i, 'A')
elif 'B' in S:
    for i in 'CDF':
        S = S.replace(i, 'B')
elif 'C' in S:
    for i in 'DF':
        S = S.replace(i, 'C')
else:
    S = 'A' * len(S)
print(S)