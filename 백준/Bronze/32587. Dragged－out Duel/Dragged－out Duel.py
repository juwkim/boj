n = int(input())
a, b = 0, 0
for l in zip(input(), input()):
    if l in (("R", "S"), ("S", "P"), ("P", "R")):
        a += 1
    elif l in (("S", "R"), ("P", "S"), ("R", "P")):
        b += 1
if a > b:
    print("victory")
else:
    print("defeat")