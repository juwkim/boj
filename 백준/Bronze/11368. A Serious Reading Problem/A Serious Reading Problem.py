while (s:=input()) != '0 0 0 0':
    C, W, L, P = map(int, s.split())
    print(((C**W)**L)**P)