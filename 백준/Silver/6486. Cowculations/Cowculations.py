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
                        t = d[c][num1[i]]
                        if len(t) == 2: t, c = t
                        else: c = ""
                    else: t = num1[i]
                    t = d[t][num2[i]]
                    if len(t) == 2: t, c = t
                    num2[i] = t
                if c:
                    num2.append(c)
            case 'R': num2 = num2[1:] + ['V']
            case 'L': num2 = ['V'] + num2
    my = "V" * (8 - len(num2)) + ''.join(num2[::-1])
    print("YES" if input() == my else "NO")