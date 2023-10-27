happy = set("HAPPY")
sad = set("SAD")

h, g = 0, 0
for c in input():
    if c in happy:
        h += 1
    if c in sad:
        g += 1
if h == 0 and g == 0:
    ans = 50
else:
    ans = h * 100 / (h + g)
print("%.2f" % ans)
