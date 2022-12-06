while n := int(input()):
    print(f'Printing order for {n} pages:')
    full_sheet, first_sheet = divmod(n, 4)
    if first_sheet == 0:
        for i in range(full_sheet):
            print(f'Sheet {i+1}, front: {n - 2*i}, {1 + 2*i}')
            print(f'Sheet {i+1}, back : {2 + 2*i}, {n - 2*i - 1}')
    elif first_sheet == 1:
        print('Sheet 1, front: Blank, 1')
        if n > 1:
            print('Sheet 1, back : 2, Blank')
            print('Sheet 2, front: Blank, 3')
            print(f'Sheet 2, back : 4, {n}')
            for i in range(full_sheet-1):
                print(f'Sheet {i+3}, front: {n - 1 - 2*i}, {5 + 2*i}')
                print(f'Sheet {i+3}, back : {6 + 2*i}, {n - 2 - 2*i}')
    elif first_sheet == 2:
        print('Sheet 1, front: Blank, 1')
        print('Sheet 1, back : 2, Blank')
        for i in range(full_sheet):
            print(f'Sheet {i+2}, front: {n - 2*i}, {3 + 2*i}')
            print(f'Sheet {i+2}, back : {4 + 2*i}, {n - 2*i - 1}')
    else:
        print('Sheet 1, front: Blank, 1')
        print(f'Sheet 1, back : 2, {n}')
        for i in range(full_sheet):
            print(f'Sheet {i+2}, front: {n - 1 - 2*i}, {3 + 2*i}')
            print(f'Sheet {i+2}, back : {4 + 2*i}, {n - 2 - 2*i}')
    print('')