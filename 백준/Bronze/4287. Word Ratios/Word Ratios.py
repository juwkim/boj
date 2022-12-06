while  (s:=input()) != '#':
    A, B, C = s.split()
    keys = [(ord(x)-ord(y))%26 for x,y in zip(B, A)]
    D = ''.join(chr(97+(ord(x)+y-97)%26) for x, y in zip(C, keys))
    print(s, D)