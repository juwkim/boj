for S, C in map(str.split, open(0)):
    match C:
        case 'K': a = (1, 4)[int(S) > 1]
        case 'N': a = (1, 2)[int(S) > 2]
        case 'B': a = S
        case 'R': a = S
    print(a)