a=[0]*11
for l in open(0):
 for i,c in enumerate(l.split()):a[i]^=int(c)
print(*a)