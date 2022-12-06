a = {'C': 12.01, 'H': 1.008, 'O': 16.00, 'N': 14.01}
for _ in range(int(input())):
    molecule, mass = input(), 0
    now, check = molecule[0], ''
    for i in range(1, len(molecule)):
        if '0' <= molecule[i] <= '9':
            check += molecule[i]
        else:
            if check:
                mass += a[now] * int(check)
            else:
                mass += a[now]
            now, check = molecule[i], ''
    if check:
        mass += a[now] * int(check)
    else:
        mass += a[now]
    print(f'{mass:#.3f}')