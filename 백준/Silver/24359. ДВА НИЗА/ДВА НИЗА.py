s, t = input(), input()

p = 0
for i in range(len(s)):
    s = s[-1] + s[:-1]
    p = max(p, s, key=int)

q = None
for j in range(len(t)):
    t = t[-1] + t[:-1]
    if t[0] != '0':
        if q == None:
            q = t
        else:
            q = min(q, t, key=int)
print(int(p) - int(q))