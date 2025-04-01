import sys
input = sys.stdin.readline

px = [0]
for _ in range(int(input())):
    s = input()
    match s[0]:
        case '+': px.append(px[-1] + int(s[1:]))
        case '-': print(px.pop() - px[-1])
        case '?': print(px[-1] - px[-int(s[1:])-1])