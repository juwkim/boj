s=0
for c in input():
 if c=='*':break
 s+=') ('.index(c)-1
print(s)