for _ in range(int(input())):
    order = input()
    s = input()
    for c in order[::-1]:
        match c:
            case 'J':
                s = s[-1] + s[:-1]
            case 'C':
                s = s[1:] + s[0]
            case 'E':
                if len(s) & 1:
                    s = s[len(s)//2+1:] + s[len(s)//2] + s[:len(s)//2]
                else:
                    s = s[len(s)//2:] + s[:len(s)//2]
            case 'A':
                s = s[::-1]
            case 'P':
                s = ''.join(c if c.isalpha() else "9012345678"[int(c)] for c in s)
            case 'M':
                s = ''.join(c if c.isalpha() else "1234567890"[int(c)] for c in s)
    print(s)