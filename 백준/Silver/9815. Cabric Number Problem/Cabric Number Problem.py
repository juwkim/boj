while (N:= input()) != '-1':
    print(f'N={int(N)}:')
    if N[0] == '0' or len(N) != 4 or len(set(N)) == 1:
        print('No!!')
    else:
        cnt = 0
        while True:
            cnt += 1
            a = int(''.join(sorted(N, reverse=True)))
            b = int(''.join(sorted(N)))
            N = str(a - b)
            print(f'{a}-{b}={N}')
            
            if N == '0' or N == '6174':
                print(f'Ok!! {cnt} times')
                break