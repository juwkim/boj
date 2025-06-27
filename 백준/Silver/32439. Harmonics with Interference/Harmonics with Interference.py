from itertools import product

str_M = input()
str_N = input()
star_pos = [('M', i) for i, c in enumerate(str_M) if c == '*']
star_pos.extend(('N', i) for i, c in enumerate(str_N) if c == '*')

for bits in product('01', repeat=len(star_pos)):
    M = list(str_M)
    N = list(str_N)
    for idx, b in enumerate(bits):
        typ, pos = star_pos[idx]
        if typ == 'M':
            M[pos] = b
        else:
            N[pos] = b
    Mint = int(''.join(M), 2)
    Nint = int(''.join(N), 2)
    if Mint % Nint == 0:
        print(''.join(M))
        break