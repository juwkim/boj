while (s:=input()) != '#':
    if s.count('A') >= len(s)/2:
        print('need quorum')
    else:
        y, n = s.count('Y'), s.count('N')
        print('yes' if y > n else 'no' if y < n else 'tie')