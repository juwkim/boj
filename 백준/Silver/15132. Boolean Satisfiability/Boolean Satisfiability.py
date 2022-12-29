positive, negative = set(), set()
negate = False
for c in input():
    if c == '|':
        continue
    if c == '~':
        negate = True
    elif negate:
        negative.add(c)
        negate = False
    else:
        positive.add(c)
ans = (1 << len(positive | negative)) - (len(positive & negative) == 0)
print(ans)  