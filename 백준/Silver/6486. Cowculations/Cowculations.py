import sys
input = lambda: sys.stdin.readline().rstrip()

d = {
    'V': {'V': 'V', 'U': 'U', 'C': 'C', 'D': 'D'},
    'U': {'V': 'U', 'U': 'C', 'C': 'D', 'D': 'VU'},
    'C': {'V': 'C', 'U': 'D', 'C': 'VU', 'D': 'UU'},
    'D': {'V': 'D', 'U': 'VU', 'C': 'UU', 'D': 'CU'}
}

for _ in range(int(input())):
    num1, num2 = [*input()[::-1]], [*input()[::-1]]
    for _ in range(3):
        match input():
            case 'A':
                c = ""
                for i in range(len(num1)):
                    if c:
                        tmp = d[c][num1[i]]
                        if len(tmp) == 2:
                            tmp, c = tmp
                        else:
                            c = ""
                    else:
                        tmp = num1[i]
                    tmp = d[tmp][num2[i]]
                    if len(tmp) == 2:
                        tmp, c = tmp
                    num2[i] = tmp
                if c:
                    num2.append(c)
            case 'R':
                num2 = num2[1:] + ['V']
            case 'L':
                num2 = ['V'] + num2
    ans = input()
    my = "V" * (8 - len(num2)) + ''.join(num2[::-1])
    if ans == my:
        print("YES")
    else:
        print("NO")