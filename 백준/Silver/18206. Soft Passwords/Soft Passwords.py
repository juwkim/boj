s = input()
p = input()
if s == p or s == p.swapcase() or (s[0].isnumeric() and s[1:] == p) or (s[-1].isnumeric() and s[:-1] == p):
    print('Yes')
else:
    print('No')