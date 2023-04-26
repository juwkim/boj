while (s:= input()) != '-1':
    n, m, k = map(int, s.split(','))
    buf = [1] * m + [0] * (n - m)
    for _ in range(k):
        new = [a^b for a, b in zip(buf, buf[1:])]
        new.append(buf[0] ^ buf[-1])
        buf = new
    print(f'{s}: {buf.count(1)}')