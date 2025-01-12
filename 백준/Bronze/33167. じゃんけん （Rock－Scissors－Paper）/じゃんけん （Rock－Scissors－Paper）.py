N = int(input())
a, b = 0, 0
for l in map("".join, zip(input(), input())):
    if l in ("RS", "SP", "PR"):
        a += 1
    elif l in ("SR", "PS", "RP"):
        b += 1
print(a, b)