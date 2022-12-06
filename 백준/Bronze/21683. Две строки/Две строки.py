s, t = input(), input()

a = 0
l = len(s)
s += s
for i in range(l):
    a = max(a, int(s[i:i+l]))

b = 1e3001
l = len(t)
t += t
for i in range(l):
    if t[i] != '0':
        b = min(b, int(t[i:i+l]))
    
print(a - b)