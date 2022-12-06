ops = set('+-*=')
cnt = 0
while True:
    try:
        r1, r2, r3 = 0, 0, '+'
        s = input()
        
        for i in range(len(s)):
            if s[i] in ops:
                r1 = eval(f'{r1}{r3}{r2}')
                if r1 < 0 or r1 >= 10000:
                    r1 = 'E'
                    break
                r2 = 0
                r3 = s[i]
            else:
                r2 = r2 * 10 + int(s[i])
                if r2 < 0 or r2 >= 10000:
                    r1 = 'E'
                    break
        print(r1)
    except:
        break