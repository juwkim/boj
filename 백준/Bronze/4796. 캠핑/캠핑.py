i = 1
while (s := input()) != '0 0 0':
    L, P, V = map(int, s.split())
    r, q = divmod(V, P)
    print(f'Case {i}: {r * L + min(L, q)}')
    i += 1