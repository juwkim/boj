while (N:= [*input()]) != ['0']:
    idx = max(range(len(N)), key=lambda x: (N[x], -x))
    if N[idx] in '13579':
        N[idx] = '0'
    else:
        N[idx] = str((int(N[idx]) + 4) % 10)
    print(int(''.join(N)))