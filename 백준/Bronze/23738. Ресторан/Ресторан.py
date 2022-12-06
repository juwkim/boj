s = input()
for a, b in zip('BHPCYX', 'vnrsuh'):
    s = s.replace(a, b)
print(s.replace('E', 'ye').lower())