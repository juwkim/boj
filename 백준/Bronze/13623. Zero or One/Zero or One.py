a, s = input(), 'A B C'
print(s[a.index('0')] if a.count('0') == 1 else s[a.index('1')] if a.count('1') == 1 else '*')