for _ in range(int(input())):
    a, b = input().split()
    if (b:=int(b)) > 96:
        s = 'A+'
    elif b > 89:
        s = 'A'
    elif b > 86:
        s = 'B+'
    elif b > 79:
        s = 'B'
    elif b > 76:
        s = 'C+'
    elif b > 69:
        s = 'C'
    elif b > 66:
        s = 'D+'
    elif b > 59:
        s = 'D'
    else:
        s = 'F'
    print(a, s)