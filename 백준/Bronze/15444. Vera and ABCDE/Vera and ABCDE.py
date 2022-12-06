g = lambda S, x, y: S.replace(x, y)
h = lambda a, b, c, d, e: g(g(g(g(g(S, 'A', a), 'B', b), 'C', c), 'D', d), 'E', e)
p, q, r = '***', '*.*', '*..'
print('***' * int(input()))
S = input()
print(h(q, q, r, q, r))
print(h(p, p, r, q, p))
print(h(q, q, r, q, r))
print(h(q, p, p, p, p))