from itertools import product

def solve():
    s = [*input()]
    idxs = [i for i, c in enumerate(s) if c == '?']
    for i in range(3):
        s[idxs[i]] = '=='
        for p in product('+-*', repeat=2):
            j = 0
            for a in p:
                if i == j:
                    j += 1
                s[idxs[j]] = a
                j += 1
            l = ''.join(s)
            if eval(l):
                return l.replace('==', '=')
    return "EI SAA"

print(solve())