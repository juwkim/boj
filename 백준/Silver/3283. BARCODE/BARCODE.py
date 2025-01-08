def solve():
    input()
    t, prv = [], None
    for col in zip(*[input() for _ in range(5)]):
        if '.' in col:
            t.append('.')
        elif 'X' in col:
            t.append('X')
        else:
            t.append('?')
    p = len(t)
    def f(l):
        for i in range(p):
            if l[i] == '?':
                if 1 <= i < p - 1:
                    if l[i - 1] == l[i + 1] == '.':
                        l[i] = 'X'
                        continue
                    if l[i - 1] == l[i + 1] == 'X':
                        l[i] = '.'
                        continue
                if i < p - 2:
                    if l[i + 1] == l[i + 2] == '.':
                        l[i] = 'X'
                        continue
                    if l[i + 1] == l[i + 2] == 'X':
                        l[i] = '.'
                        continue
                if i > 1:
                    if l[i - 1] == l[i - 2] == '.':
                        l[i] = 'X'
                        continue
                    if l[i - 1] == l[i - 2] == 'X':
                        l[i] = '.'
                        continue
        return l
    t = f(t)
    t = f(t[::-1])[::-1]
    if '?' in t:
        return 'UNDETERMINABLE'
    ans, prv = [], None
    for c in t:
        if c == prv:
            ans.pop()
            ans.append('1')
        else:
            ans.append('0')
        prv = c
    return ''.join(ans)
print(solve())