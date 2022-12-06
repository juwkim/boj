cnt = 1
while (s:= input()) != '0 0 0 0':
    Z, I, M, L = map(int, s.split())
    idx, buf = 0, {}
    while L not in buf:
        buf[L] = idx
        L = (Z * L + I) % M
        idx += 1
    print(f'Case {cnt}: {idx - buf[L]}')
    cnt += 1