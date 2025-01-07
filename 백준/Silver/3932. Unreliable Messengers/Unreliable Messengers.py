for _ in range(int(input())):
    order = input()
    l = len(s:=[*input()])
    for c in order[::-1]:
        match c:
            case 'J': s = [s[-1]] + s[:-1]
            case 'C': s = s[1:] + [s[0]]
            case 'E': s = (s[l//2+1:] + [s[l//2]] if l & 1 else s[l//2:]) + s[:l//2]
            case 'A': s = s[::-1]
            case 'P': s = [c if c.isalpha() else "9012345678"[int(c)] for c in s]
            case 'M': s = [c if c.isalpha() else "1234567890"[int(c)] for c in s]
    print(*s, sep='')