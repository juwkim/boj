input()
s = sorted(i for i in input() if i != '0')
p, q = s[::2], s[1::2]
a = int(''.join(p)) if p else 0
b = int(''.join(q)) if q else 0
print(a + b)