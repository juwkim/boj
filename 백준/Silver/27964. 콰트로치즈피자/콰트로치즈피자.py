a = set()
input()
for s in input().split():
    if s.endswith('Cheese'):
        a.add(s)
if len(a) >= 4:
    print('yummy')
else:
    print('sad')