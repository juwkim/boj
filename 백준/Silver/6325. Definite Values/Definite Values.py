cnt = 1
while N:= int(input()):

    check = {'a'}
    for _ in range(N):
        new, old = input().split(' = ')
        if old in check:
            check.add(new)
        else:
            if new in check:
                check.remove(new)
    print(f'Program #{cnt}')
    if check:
        print(*sorted(check))
    else:
        print('none')
    print()
    cnt += 1