def get_dic(st):
    dic = {'C': 0, 'H': 0, 'O': 0}
    i = 0
    c, num = '', 0
    while i < len(st):
        if st[i].isalpha():
            if c:
                dic[c] += max(num, 1)
            c, num = st[i], 0
        else:
            num = num * 10 + int(st[i])
        i += 1
    if c:
        dic[c] += max(num, 1)
    return dic

def solve():
    for x  in range(1, 11):
        for y in range(1, 11):
            for z in range(1, 11):
                if all(x * p[i] + y * q[i] == z * r[i] for i in 'CHO'):
                    print(x, y, z)
                    return

s = input()
a, b = s.index('+'), s.index('=')
p, q, r = get_dic(s[:a]), get_dic(s[a+1:b]), get_dic(s[b+1:])
solve()