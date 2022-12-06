s = input()
n = len(s)
s = s + s[0]
x, y = 0, 0
for i in range(n):
    a = s[i:i+2]
    x += (a == '00')
    y += (a == '01')
p = x / (x + y)
q = s[:-1].count('0') / n
print(['EQUAL', 'SHOOT', 'ROTATE'][(p > q) - (p < q)])