g = lambda: [*map(int, input().split())]



s1, g1, a1 = g()
s2, g2, a2 = g()

if a1 == -1:
    if g1 != -1 and s2 != -1:
        a1 = s2 + g1
elif a1 == 0:
    g1 = 0
    s2 = 0
if a2 == -1:
    if g2 != -1 and s1 != -1:
        a2 = s1 + g2
elif a2 == 0:
    g2 = 0
    s1 = 0

if g1 == -1:
    if a1 != -1 and s2 != -1:
        g1 = a1 - s2
if g2 == -1:
    if a2 != -1 and s1 != -1:
        g2 = a2 - s1
if s1 == -1:
    if a2 != -1 and g2 != -1:
        s1 = a2 - g2
if s2 == -1:
    if a1 != -1 and g1 != -1:
        s2 = a1 - g1
print(s1, g1, a1)
print(s2, g2, a2)