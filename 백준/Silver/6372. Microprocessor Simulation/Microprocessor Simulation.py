while True:
    try:
        s = input()
        if s[0] == '8':
            break
        mem = [int(x, 16) for x in s]
        i = 0
        A, B = 0, 0
        while True:
            match mem[i]:
                case 0:
                    pos = mem[i+1] * 16 + mem[i+2]
                    A = mem[pos]
                    i += 3
                case 1:
                    pos = mem[i+1] * 16 + mem[i+2]
                    mem[pos] = A
                    i += 3
                case 2:
                    A, B = B, A
                    i += 1
                case 3:
                    B, A = divmod(A + B, 16)
                    i += 1
                case 4:
                    A = (A + 1) % 16
                    i += 1
                case 5:
                    A = (A - 1) % 16
                    i += 1
                case 6:
                    if A == 0:
                        i = mem[i+1] * 16 + mem[i+2]
                    else:
                        i += 3
                case 7:
                    i = mem[i+1] * 16 + mem[i+2]
                case 8:
                    break
        print(*["0123456789ABCDEF"[i] for i in mem], sep="")
    except EOFError:
        break