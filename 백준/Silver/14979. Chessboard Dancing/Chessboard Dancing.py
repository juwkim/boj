for S, C in map(str.split, open(0)):
    S = int(S)
    match C:
        case 'K':
            if S > 1:
                ans = 4
            else:
                ans = 1
        case 'N':
            if S > 2:
                ans = 2
            else:
                ans = 1
        case 'B':
            ans = S
        case 'R':
            ans = S
    print(ans)