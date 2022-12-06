buf = []
while (s:= input())[0] != '-':
    A, U, R, *V = s.split()
    A, R = map(float, [A, R])
    amount = A * 100 / R
    if amount < 1:
        buf.append(V)
    else:
        print(f'{" ".join(V)} {A:.1f} {U} {amount:.0f}%')
print('Provides no significant amount of:')
for item in buf:
    print(*item)