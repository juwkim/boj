a=set()
for l in open(0):a.add(''.join(l.split()[1:]))
print(len(a))