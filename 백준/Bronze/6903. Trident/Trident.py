t, s, h = [int(input()) for _ in range(3)]
txt = '*' + ' ' * s + '*' + ' ' * s + '*'
for _ in range(t):
    print(txt)

print('*' * (2 * s + 3))

txt = ' ' * (s + 1) + '*'
for _ in range(h):
    print(txt)