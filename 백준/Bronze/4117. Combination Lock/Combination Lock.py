while (s:= input()) != '0 0 0 0':
    N, T1, T2, T3 = map(int, s.split())
    print(4 * N - 1 + (T2 - T1) % N + (T2 - T3) % N)