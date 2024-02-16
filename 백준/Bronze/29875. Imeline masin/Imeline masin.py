input()
s = [1, 0, 0, 0]
for c in map(int, input().split()):
    match c:
        case 0:
            s = [s[1], s[0], 0, s[2] | s[3]]
        case 1:
            s = [s[3], s[0], s[1] | s[2], 0]
        case -1:
            s = [s[1] | s[3], s[0], s[1] | s[2], s[2] | s[3]]
for c in s:
    print(("EI", "JAH")[c])