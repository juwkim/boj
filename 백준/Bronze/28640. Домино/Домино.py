a1, b1 = map(len, input().split('|'))
a2, b2 = map(len, input().split('|'))
print(('No','Yes')[a1 in (a2, b2) or b1 in (a2, b2)])